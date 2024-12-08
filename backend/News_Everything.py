'''
This is the module for all categories news which fetch the news sources and use ChatGPT to summarize the news.
In order to run the task, it's required to include the ChatGPT and NewsAPI crentials in the .env file for setting up the environment variables.
'''
import requests
import os
from Database import DB_operation
import re
import json
import requests
from dotenv import load_dotenv

class NewsApi():
    def __init__(self, query_news, news_api, openai_api, id='1'):
        #query_news: the dictionary of each category with its keywords
        if type(query_news) != dict:
            raise TypeError(f'The input query_news: {query_news} should be dictionary type.')
        self.query_news = query_news
        #news_api: the credential for NewsApi
        if type(news_api) != str:
            raise TypeError(f'The input news_api: {news_api} should be string type.')
        self.news_api = news_api
        #openai_api: the credential for ChatGPT
        if type(openai_api) != str:
            raise TypeError(f'The input openai_api: {openai_api} should be string type.')
        self.openai_api = openai_api
        #id: the index for the data to store in the table
        if type(id) != str:
            raise TypeError(f'The input id: {id} should be string type.')
        self.id = id
        #db_operation: the instance of the Database module
        self.db_operation = DB_operation()

    def str_cleansing(self, text):
    #Cleanse the strings
        if type(text) != str:
            raise TypeError(f'The input text: {text} should be string type.')
        cleaned_content = re.sub(r"\[.*?\]", "", text)
        cleaned_content = re.sub(r"</?ul>|</?li>|\r|\n|\.{3}|…", "", cleaned_content)
        cleaned_content = re.sub(r"\s{2,}", " ", cleaned_content)
        cleaned_content = cleaned_content.strip()
        return cleaned_content
    
    def write_json(self, data, filename):
    #Write data to json file
        if type(filename) != str:
            raise TypeError(f'The input filename: {filename} should be string type.')
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Dictionary saved to {filename}")

    def read_json(filename):
    #Read data from json file
        if type(filename) != str:
            raise TypeError(f'The input filename: {filename} should be string type.')
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    
    def newsapi_call(self, query):
    #Call the News API endpoints
        if type(query) != str:
            raise TypeError(f'The input query: {query} should be string type.')
        data = []
        news_get_request = requests.get(f'https://newsapi.org/v2/everything?q={query}&apiKey={self.news_api}&language=en')
        news_json = news_get_request.json()
        seen_titles = set()
        print('news_json: ', news_json)
        for article in news_json['articles']:
            if (article['description'] is not None) and (article['content'] is not None) and (article['content'] != '[Removed]'):
                if article["title"] not in seen_titles:
                    description = self.str_cleansing(article['description'])
                    content = self.str_cleansing(article['content'])
                    data.append({'title': article['title'], 'description': description, 'url': article['url'], 'content': content})
                    seen_titles.add(article['title'])
                    print("Include the new article: ", article['title'])
                else:
                    print('duplicates found')
                    continue
            else:
                print('find null values')
                continue
        return data
    
    def news_aggregate(self):
    #Aggregate all the news it collected
        news_dict = {key: [] for key in self.query_news.keys()}
        for key in self.query_news.keys():
            for query in self.query_news[key]:
                everything_data = self.newsapi_call(query)
                news_dict[key].extend(everything_data)
        return news_dict
    
    def add_index(self, data):
    #Add the index to each news
        if type(data) != dict:
            raise TypeError(f'The input data: {data} should be dictionary type.')
        for key in data.keys():
            index = 0
            for news in data[key]:
                news['index'] = index
                index+=1
        self.write_json(news_dict, 'news_dict_keywords.json')
        return data
    
    def remove_url(self, data):
    #Remove url from the data before feeding to Chatgpt
        if type(data) != dict:
            raise TypeError(f'The input data: {data} should be dictionary type.')
        for key in data.keys():
            for news in data[key]:
                del news["url"]
        return data
    
    def openai_api_call(self, data_category, model):
    #Call ChatGPT API
        if type(data_category) != str:
            raise TypeError(f'The input data_category: {data_category} should be string type.')
        if type(model) != str:
            raise TypeError(f'The input model: {model} should be string type.')
        if self.openai_api is None:
            raise ValueError("OpenAI API key is not set in environment variables.")
        url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.openai_api}"
        }
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": """
                    You are the agent that generates JSON. You always return just the JSON with no additional description or context.
                    Please respond only with JSON data, without any code blocks or formatting such as ```json ```.
                    You have a list of dictionaries consisting of the news information, including title, description, content and index in JSON format as input.
                    Group the news by topic where each topic has at most 10 news.
                    Provide the list of keywords for each news.
                    Provide the summary for the topic.
                    Rate the bias of each news item on a scale of 0-10,
                    where 0-3 indicates left-leaning, 4-6 indicates neutral, and 7-10 indicates right-leaning.
                    Each news should belong to a topic. The topic can be specific or general.
                    The output should be in the following format:
                    {"item": [
                        {
                            "topic": "name of the topic"
                            "summary": "summary of the topic",
                            "news_sources": [
                                {
                                "index": "index of the news",
                                "keywords": ["keywords of the news"],
                                "bias": "bias of the news"
                                }
                            ]
                        }
                        ]
                    }
                """},
                {
                    "role": "user",
                    "content": f'{data_category}'
            }]
        }
        response = requests.post(url, headers=headers, json=data)
        # Check if the request was successful
        if response.status_code == 200:
            print("Response from OpenAI:", response.json())
            print('\n')
            print(response.json()['choices'][0]['message']['content'])
        else:
            print("Error:", response.status_code, response.text)
        return json.loads(response.json()['choices'][0]['message']['content'])
    
    def iter_call_chatgpt(self, news_dict):
    #Iterative over each news category to call ChatGPT API and retrieve back the response
        if type(news_dict) != dict:
            raise TypeError(f'The input news_dict: {news_dict} should be dictionary type.')
        final_output = {}
        for key in news_dict.keys():
            data_category = news_dict[key]
            try:
                parsed_json = self.openai_api_call(data_category, 'gpt-4o-mini')
            except Exception as e:
                print(f"An error occurred on gpt-4-turbo call: {e}")
                try:
                    parsed_json = self.openai_api_call(data_category, 'gpt-4o-2024-08-06')
                except Exception as e:
                    print(f"An error occurred on gpt-4o-2024-08-06 call: {e}")
                    try:
                        parsed_json = self.openai_api_call(data_category, 'gpt-4-turbo')
                    except Exception as e:
                        print(f"An error occurred on gpt-4o-mini call: {e}")
                        print('All of the selected GPT models failed!')
                        pass
            final_output[key] = parsed_json
            final_output[key]['urlToImage'] = ''
        final_output['id'] = self.id
        #access the table in dynamoDB. Write the data to the database
        self.db_operation.write(f'categories_news', final_output)
        return final_output

if __name__ == '__main__':
    # Load the environment variables for credentials
    load_dotenv()
    news_api = os.getenv('news_apiKey')
    print('news_api: ', news_api)
    openai_api = os.getenv('openai_api_key')
    print('openai_api: ', openai_api)
    query_news = \
        {
        "business": ["economy"],
        "entertainment": ["movies"],
        "general": ["politics"],
        "health": ["health"],
        "science": ["science"],
        "sports": ["basketball"],
        "technology": ["technology"]
        }
    news_everything = NewsApi(query_news=query_news, news_api=news_api, openai_api=openai_api, id='2')
    news_dict = news_everything.news_aggregate()
    news_dict = news_everything.add_index(news_dict)
    news_everything.write_json(news_dict, 'news_dict_keywords.json')
    news_dict = news_everything.remove_url(news_dict)
    final_output = news_everything.iter_call_chatgpt(news_dict)