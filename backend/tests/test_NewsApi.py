import pytest
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from News_Everything import NewsApi

def test_attribute():
    query_news = {
        "business": ["economy"]
    }
    news_api = '123'
    openai_api = '123'
    news_everything = NewsApi(query_news, news_api, openai_api)
    assert type(news_everything.query_news) == dict
    assert type(news_everything.openai_api) == str
    assert type(news_everything.news_api) == str

def test_str_cleansing():
    raw_text = "This is the sentence contains some unwanted text such as [word1] <li>word2</li> and white  spaces.  "
    news_api = '123'
    openai_api = '123'
    id='2'
    newsapi = NewsApi({ "business": ["economy"]}, news_api, openai_api, id)
    cleaned_text = newsapi.str_cleansing(raw_text)
    print(cleaned_text)
    assert cleaned_text == "This is the sentence contains some unwanted text such as word2 and white spaces."

def test_remove_url():
    raw_text = {
        'test_key': [
            {'text':[1,2,3], 
             'url': 'https'}
                              ]
                              }
    news_api = '123'
    openai_api = '123'
    id='2'
    newsapi = NewsApi({ "business": ["economy"]}, news_api, openai_api, id)
    newsapi.remove_url(raw_text)
    assert 'url' not in raw_text['test_key'][0].keys()

def test_db_response():
    id='1'
    news_api = '123'
    openai_api = '123'
    news = NewsApi({ "business": ["economy"]}, news_api, openai_api, id)
    table = news.dynamodb.Table(f'categories_news')
            #Fetch the headlines
    response = table.get_item(
        Key={
            'id': news.id
        }
    )
    assert type(response) == dict