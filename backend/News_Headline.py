import requests
import boto3
import os
from dotenv import load_dotenv
from database import DB_operation


class Headline():
    def __init__(self, news_api, id='1'):
        # Init
        self.news_api = news_api
        self.id = id
        self.dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
        self.db_operation = DB_operation()

    def call_api(self, category_list=['business']):
            # /v2/top-headlines
            #categories: business|entertainment|general|health|science|sports|technology 
            for category in category_list:
                print(f'Start fetching data for {category}')
                news_get_request = requests.get(f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={self.news_api}')
                news_json = news_get_request.json()
                news_json['id'] = self.id
                #access the table in dynamoDB. write the data to the database
                self.db_operation.write(f'top_news', news_json)

if __name__ == '__main__':
    # Load the environment variables for credentials
    load_dotenv()
    news_api = os.getenv('news_apiKey')
    print('news_api: ', news_api)
    headline = Headline(news_api, id='1')
    headline.call_api()