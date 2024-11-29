import json
import openai
import boto3
from database import DB_operation
import os

class Headline_Keywords():
    def __init__(self):
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.time_table = self.dynamodb.Table('time')
        self.db_operation = DB_operation()
        response = self.db_operation.lambda_handler(self.time_table)
        self.time = response['Items'][0]['time']

    def call_chatgpt(self):
        for category in ['business','entertainment','general','health','science','sports','technology']:
            print(f'Start fetching data for {category}')
            table = self.dynamodb.Table(f'{category}-top-headlines')
            #Fetch the headlines
            response = table.get_item(
                Key={
                    'id':'1',
                    'date_time': self.time
                }
            )
            #Preprocess the headlines into the format for ChatGPT
            data = response['Item']['articles']
            headlines_lst = []
            for list_dict in data:
                dict1 = {}
                dict1['description'] = list_dict['description']
                dict1['title'] = list_dict['title']
                dict1['content'] = list_dict['content']
                headlines_lst.append(dict1)
            headlines_lst = str(headlines_lst)

            # Set up your API key
            #Initiate ChatGPT API
            openai_api_key = os.environ.get('openai_api_key')
            openai.api_key = openai_api_key

            response = openai.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": """
                        You are the agent that generate JSON. You always return just the JSON as follows with no additional description or context.
                        You have a list of headlines including title, url, description and brief content in JSON format as input.
                        Provide the key words for the headline as follows:
                        {'headlines': [
                            {
                                "title": "title_1",
                                "keywords": ["keyword_1", "keyword_2"...]
                            },
                            {
                                "title": "title_2",
                                "keywords": ["keyword_1", "keyword_2"...]
                            }
                        ]}
                    """},
                {"role": "user", "content": headlines_lst}
            ],
            response_format={"type": "json_object"}
            )


            # Parse ChatGPT JSON output into a Python dictionary
            parsed_json = json.loads(response.choices[0].message.content)
            
            ### Include the keywords by ChatGPT into the original headlines table
            
            response = self.db_operation.read(f'{category}-top-headlines', self.time)
            headlines_news = response['Item']
            headline_keywords = {'totalResults':headlines_news['totalResults'], 'date_time':headlines_news['date_time'], 'articles':[]}
            for headline in headlines_news['articles']:
                try:
                    for chatgpt_headline in parsed_json['headlines']:
                        if chatgpt_headline['title'] == headline['title']:
                            headline['keywords'] = chatgpt_headline['keywords']
                            headline_keywords['articles'].append(headline)
                            break
                except Exception as e:
                    print("An error occurred:", e)
                    break
            headline_keywords['id'] = '1'
            headline_keywords['date_time'] = self.time
            #access the table in dynamoDB
            self.db_operation.write(f'{category}-top-headlines', headline_keywords)
            