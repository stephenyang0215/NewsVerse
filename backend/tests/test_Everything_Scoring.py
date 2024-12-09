'''
This is the testing file for the Everything_Scoring module.
In order to run the test_db_response function, it's required to set up AWS crentials configuration in advance.
'''
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from Everything_Scoring import Everything_Scoring

#test the attribute of the module
def test_attribute():
    openai_api = '123'
    id = '1'
    news_everything = Everything_Scoring(openai_api, id)
    assert type(news_everything.openai_api) == str
    assert type(news_everything.id) == str

#test the url removal function
def test_remove_url():
    raw_text = {
        'business': [
            {'text':[1,2,3], 
             'url': 'https'}
                              ]
                              }
    openai_api = '123'
    id='2'
    newsapi = Everything_Scoring(openai_api, id)
    raw_text = newsapi.remove_url(raw_text)
    assert 'url' not in raw_text['business'][0].keys()

#test the data it reads from the database
def test_db_response():
    id='1'
    openai_api = '123'
    news = Everything_Scoring(openai_api, id)
    data = news.db_operation.read(f'categories_news', id)
    assert type(data) == dict