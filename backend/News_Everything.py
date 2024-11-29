import requests
import boto3
import os
from os.path import join, dirname
import re
import json
import requests
from dotenv import load_dotenv, find_dotenv

class news():
    def __init__(self, query_news, news_api, openai_api):
        self.query_news = query_news
        self.news_api = news_api
        self.openai_api = openai_api

    def str_cleansing(self, text):#preprocess the news
        cleaned_content = re.sub(r"\[.*?\]", "", text)
        cleaned_content = re.sub(r"</?ul>|</?li>|\r|\n|\.{3}|…", "", cleaned_content)
        cleaned_content = re.sub(r"\s{2,}", " ", cleaned_content)
        cleaned_content = cleaned_content.strip()
        return cleaned_content
    
    def write_json(self, data, filename):
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Dictionary saved to {filename}")

    def read_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    
    def newsapi_call(self, query):
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
        #aggregate all the news from the calls
        news_dict = {key: [] for key in self.query_news.keys()}
        for key in self.query_news.keys():
            for query in self.query_news[key]:
                everything_data = self.newsapi_call(query)
                news_dict[key].extend(everything_data)
        return news_dict
    
    #add the index to each news
    def add_index(self, data):
        for key in data.keys():
            index = 0
            for news in data[key]:
                news['index'] = index
                index+=1
        self.write_json(news_dict, 'news_dict_keywords.json')
        return data
    
    #reformat the data to chatgpt api: remove url
    def remove_url(self, data):
        for key in data.keys():
            for news in data[key]:
                del news["url"]
        return data
    
    #Call ChatGPT API
    def openai_api_call(self, data_category, model):
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
        #Call Chatgpt API to fetch the response iteratively by all categories
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
    news_everything = news(query_news=query_news, news_api=news_api, openai_api=openai_api)
    news_dict = news_everything.news_aggregate()
    news_dict = news_everything.add_index(news_dict)
    news_everything.write_json(news_dict, 'news_dict_keywords.json')
    news_dict = news_everything.remove_url(news_dict)
    final_output = news_everything.iter_call_chatgpt(news_dict)
    final_output['id'] = '2'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(f'categories_news')
    table.put_item(
            Item=final_output
    )
    print(f'Data is inserted into the categories_news table successfully.')