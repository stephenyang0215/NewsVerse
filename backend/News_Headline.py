import json
from newsapi import NewsApiClient
import requests
import boto3
from datetime import datetime
import os

news_apiKey = os.environ.get('news_apiKey')
# Init
newsapi = NewsApiClient(api_key=news_apiKey)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

table = dynamodb.Table('time')
table.put_item(
        Item={'id':'1', 'time':dt_string}
)


# /v2/top-headlines
#categories: business|entertainment|general|health|science|sports|technology
for category in ['business','entertainment','general','health','science','sports','technology']:
    print(f'Start fetching data for {category}')
    news_get_request = requests.get(f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={news_apiKey}')
    news_json = news_get_request.json()
    news_json['id'] = '1'
    news_json['date_time'] = dt_string
    #access the table in dynamoDB
    table = dynamodb.Table(f'{category}-top-headlines')
    table.put_item(
            Item=news_json
    )
    print(f'Data is inserted into the {category}-top-headlines table successfully.')
