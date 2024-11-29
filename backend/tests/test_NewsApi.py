import pytest
import re
import json
import sys
import os.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
from News_Everything import NewsApi

def test_attribute():
    
    query_news = {
        "business": ["economy"]
    }
    newsapi = NewsApi(query_news)
    assert type(newsapi.query_news) == dict

def test_str_cleansing():
    raw_text = "This is the sentence contains some unwanted text such as [word1] <li>word2</li> and white  spaces.  "
    newsapi = NewsApi({ "business": ["economy"]})
    cleaned_text = newsapi.str_cleansing(raw_text)
    print(cleaned_text)
    assert cleaned_text == "This is the sentence contains some unwanted text such as word2 and white spaces."