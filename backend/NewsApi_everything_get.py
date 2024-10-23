import json
from newsapi import NewsApiClient
import requests
import boto3

# Init
newsapi = NewsApiClient(api_key='')
dynamodb = boto3.resource('dynamodb')

# /v2/top-headlines
#categories: business|entertainment|general|health|science|sports|technology
for category in ['business','entertainment','general','health','science','sports','technology']:
    news_get_request = requests.get(f'https://newsapi.org/v2/top-headlines?category={category}&apiKey=')
    news_json = news_get_request.json()
    #access the table in dynamoDB
    table = dynamodb.Table(f'{category}-top-headlines')
    table.put_item(
            Item=news_json
    )
    print(f'Data is inserted into the {category}-top-headlines table successfully.')


# /v2/everything
all_articles = newsapi.get_everything(domains='bbc.co.uk,techcrunch.com',
                                      from_param='2024-09-01',
                                      to='2024-09-20',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
print('Articles fetched!')
# /v2/top-headlines/sources
sources = newsapi.get_sources()
news_get_request = requests.get('https://newsapi.org/v2/everything?&apiKey=')
news_json = news_get_request.json()

# Save to JSON file
with open("NewsApi.json", "w") as f:
    json.dump(news_json, f, indent=4)  # indent for pretty formatting

print('File saved!')