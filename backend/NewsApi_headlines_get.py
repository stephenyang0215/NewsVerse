import json
from newsapi import NewsApiClient
import requests
import boto3
from datetime import date

today = date.today().strftime("%Y-%m-%d")

# Init
newsapi = NewsApiClient(api_key='')
session = boto3.Session(
    aws_access_key_id='',
    aws_secret_access_key=''
)
dynamodb = session.resource('dynamodb')

# /v2/top-headlines
#categories: business|entertainment|general|health|science|sports|technology
for category in ['business','entertainment','general','health','science','sports','technology']:
    print(f'Start fetching data for {category}')
    news_get_request = requests.get(f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=')
    news_json = news_get_request.json()
    news_json['date'] = today
    #access the table in dynamoDB
    table = dynamodb.Table(f'{category}-top-headlines')
    table.put_item(
            Item=news_json
    )
    print(f'Data is inserted into the {category}-top-headlines table successfully.')
