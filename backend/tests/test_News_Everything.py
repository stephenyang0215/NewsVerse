'''
This is the testing file for the News_Everything module.
In order to run the test_db_response function, it's required to set up AWS crentials configuration in advance.
'''
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from News_Everything import News_Everything

#test the attribute of the module
def test_attribute():
    query_news = {
        "business": ["economy"]
    }
    news_api = '123'
    news_everything = News_Everything(query_news, news_api)
    assert type(news_everything.query_news) == dict
    assert type(news_everything.news_api) == str

#test the string cleansing function
def test_str_cleansing():
    raw_text = "This is the sentence contains some unwanted text such as [word1] <li>word2</li> and white  spaces.  "
    news_api = '123'
    id='2'
    newsapi = News_Everything({ "business": ["economy"]}, news_api, id)
    cleaned_text = newsapi.str_cleansing(raw_text)
    print(cleaned_text)
    assert cleaned_text == "This is the sentence contains some unwanted text such as word2 and white spaces."



#test the data it reads from the database
def test_db_response():
    id='1'
    news_api = '123'
    news = News_Everything({ "business": ["economy"]}, news_api, id)
    data = news.db_operation.read(f'categories_news', id)
    assert type(data) == dict