'''
This is the testing file for the Headline_keywords module.
In order to run the test_db_response function, it's required to set up AWS crentials configuration in advance.
'''
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Headline_Keywords import Headline_Keywords

#test the attribute of the module
def test_attribute():
    id = '3'
    news_api = '123'
    openai_api = '123'
    headline = Headline_Keywords(news_api, openai_api, id)
    assert type(headline.id) == str
    assert type(headline.openai_api) == str
    assert type(headline.news_api) == str

#test the data it reads from the database
def test_db_response():
    id = '1'
    news_api = '123'
    openai_api = '123'
    headline = Headline_Keywords(news_api, openai_api, id)
    data = headline.db_operation.read(f'top_news', id)
    assert type(data) == dict
