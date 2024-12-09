'''
This is the module for all categories news which fetch the news sources and use ChatGPT to summarize the news.
In order to run the task, it's required to include the ChatGPT and NewsAPI crentials in the .env file for setting up the environment variables.
'''
import requests
import os
from Database import DB_Operation
import re
import requests
from dotenv import load_dotenv

class News_Everything():
    def __init__(self, query_news, news_api, id='1'):
        #query_news: the dictionary of each category with its keywords
        if type(query_news) != dict:
            raise TypeError(f'The input query_news: {query_news} should be dictionary type.')
        self.query_news = query_news
        #news_api: the credential for NewsApi
        if type(news_api) != str:
            raise TypeError(f'The input news_api: {news_api} should be string type.')
        self.news_api = news_api
        #id: the index for the data to store in the table
        if type(id) != str:
            raise TypeError(f'The input id: {id} should be string type.')
        self.id = id
        #db_operation: the instance of the Database module
        self.db_operation = DB_Operation()

    def str_cleansing(self, text):
    #Cleanse the strings
        if type(text) != str:
            raise TypeError(f'The input text: {text} should be string type.')
        cleaned_content = re.sub(r"\[.*?\]", "", text)
        cleaned_content = re.sub(r"</?ul>|</?li>|\r|\n|\.{3}|…", "", cleaned_content)
        cleaned_content = re.sub(r"\s{2,}", " ", cleaned_content)
        cleaned_content = cleaned_content.strip()
        return cleaned_content
    
    def call_newsapi(self, query):
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
                everything_data = self.call_newsapi(query)
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
        data['id'] = self.id
        return data
    

if __name__ == '__main__':
    # Load the environment variables for credentials
    load_dotenv()
    news_api = os.getenv('news_apiKey')
    print('news_api: ', news_api)
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
    news_everything = News_Everything(query_news=query_news, news_api=news_api, id='3')
    news_dict = news_everything.news_aggregate()
    news_dict = news_everything.add_index(news_dict)
    news_everything.db_operation.write('categories_news', news_dict)