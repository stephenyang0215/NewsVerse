'''
This is the NewsApi module for the top news to fetch the latest top news.
In order to run the task, it's required to include the NewsAPI crentials in the .env file for setting up the environment variables.
'''
import requests
import os
from dotenv import load_dotenv
from Database import DB_Operation


class Headline():
    def __init__(self, news_api, id='1'):
        #news_api: the credential for NewsApi
        if type(news_api) != str:
            raise TypeError(f'The input news_api: {news_api} should be string type.')
        self.news_api = news_api
        #id: the id for the data to store in the table
        if type(id) != str:
            raise TypeError(f'The input id: {id} should be string type.')
        self.id = id
        #db_operation: the instance of the Database module 
        self.db_operation = DB_Operation()

    #call_api: fetch the top news by the category specified. This endpoint supports the following categories: business|entertainment|general|health|science|sports|technology 
    def call_newsapi(self, category_list=['business']):
            if type(category_list) not in (list):
                raise TypeError(f'The input category_list: {category_list} should be list type.')
            for category in category_list:
                if type(category) not in (str):
                    raise TypeError(f'The input category: {category} should be string type.')
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
    headline.call_newsapi()