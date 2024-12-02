import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from headline_keywords import Headline_Keywords

def test_attribute():
    id='3'
    news_api = '123'
    openai_api = '123'
    headline = Headline_Keywords(news_api, openai_api, id)
    assert type(headline.id) == str
    assert type(headline.openai_api) == str
    assert type(headline.news_api) == str

def test_db_response():
    id='3'
    news_api = '123'
    openai_api = '123'
    headline = Headline_Keywords(news_api, openai_api, id)
    table = headline.dynamodb.Table(f'top_news')
            #Fetch the headlines
    response = table.get_item(
        Key={
            'id': headline.id
        }
    )
    assert type(response) == dict