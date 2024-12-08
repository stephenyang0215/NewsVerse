'''
This is the testing file for the News_Headline module.
In order to run the test_db_response function, it's required to set up AWS crentials configuration in advance.
'''
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from News_Headline import Headline

#test the attribute of the module
def test_attribute():
    id = '4'
    news_api = '123'
    headline = Headline(news_api, id)
    assert type(headline.id) == str
    assert type(headline.news_api) == str

#test to read the data it wrote to the database
def test_db_response():
    id = '1'
    news_api = '123'
    headline = Headline(news_api, id)
    data = headline.db_operation.read(f'categories_news', id)
    assert type(data) == dict