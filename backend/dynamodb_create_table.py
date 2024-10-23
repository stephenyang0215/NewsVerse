import boto3
from newsapi import NewsApiClient
import requests

dynamodb = boto3.resource('dynamodb')
print('Connected to dynamodb!')
# Init
newsapi = NewsApiClient(api_key='')

# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          #sources='bbc-news,the-verge',
                                          #category='business',
                                          language='en')#,
                                          #country='us')
print('Top headlines fetched!')
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      #sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2024-09-01',
                                      to='2024-09-20',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
print('Articles fetched!')
# /v2/top-headlines/sources
sources = newsapi.get_sources()
news_get_request = requests.get('https://newsapi.org/v2/everything?q=bitcoin&apiKey=')
news_json = news_get_request.json()

#access the table in dynamoDB
table = dynamodb.Table('NewsApi')

table.put_item(
        Item=news_json
)
print('Data is inserted into the table successfully.')