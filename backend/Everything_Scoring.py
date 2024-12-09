'''
This is the module for all categories news which fetch the news sources and use ChatGPT to summarize the news.
In order to run the task, it's required to include the ChatGPT and NewsAPI crentials in the .env file for setting up the environment variables.
'''
import requests
import os
from Database import DB_Operation
import json
import requests
from dotenv import load_dotenv

class Everything_Scoring():
    def __init__(self, openai_api, id='1'):
        #openai_api: the credential for ChatGPT
        if type(openai_api) != str:
            raise TypeError(f'The input openai_api: {openai_api} should be string type.')
        self.openai_api = openai_api
        #id: the index for the data to store in the table
        if type(id) != str:
            raise TypeError(f'The input id: {id} should be string type.')
        self.id = id
        #db_operation: the instance of the Database module
        self.db_operation = DB_Operation()
    
    def remove_url(self, data):
    #Remove url from the data before feeding to Chatgpt
        if type(data) != dict:
            raise TypeError(f'The input data: {data} should be dictionary type.')
        for key in data.keys():
            if key not in ["business", "entertainment", "general", "health", "science", "sports", "technology"]:
                continue
            for news in data[key]:
                try:
                    del news["url"]
                except Exception as e:
                    print(f"An error occurred: {e} at key {key}")
        return data
    
    def call_chatgpt(self, data_category, model):
    #Call ChatGPT API
        if type(data_category) != list:
            raise TypeError(f'The input data_category: {data_category} should be list type.')
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
            if key not in ["business", "entertainment", "general", "health", "science", "sports", "technology"]:
                continue
            data_category = news_dict[key]
            try:
                parsed_json = self.call_chatgpt(data_category, 'gpt-4o-mini')
            except Exception as e:
                print(f"An error occurred on gpt-4-turbo call: {e}")
                try:
                    parsed_json = self.call_chatgpt(data_category, 'gpt-4o-2024-08-06')
                except Exception as e:
                    print(f"An error occurred on gpt-4o-2024-08-06 call: {e}")
                    try:
                        parsed_json = self.call_chatgpt(data_category, 'gpt-4-turbo')
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
    scoring = Everything_Scoring(openai_api=openai_api, id='3')
    news_dict = scoring.db_operation.read('categories_news', scoring.id)
    news_dict = scoring.remove_url(news_dict['Item'])
    final_output = scoring.iter_call_chatgpt(news_dict)