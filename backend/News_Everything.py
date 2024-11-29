import requests
import boto3
import os

news_apiKey = os.environ.get('news_apiKey')
# Init
dynamodb = boto3.resource('dynamodb')

# /v2/everything
#categories: business|entertainment|general|health|science|sports|technology
for general_term in ['breaking news','stock','president','business','climate','emergency','event']:
    news_get_request = requests.get(f'https://newsapi.org/v2/everything?q={general_term}&apiKey={news_apiKey}')
    news_json = news_get_request.json()
    #access the table in dynamoDB
    table = dynamodb.Table(f'{general_term}-everything')
    table.put_item(
            Item=news_json
    )
    print(f'Data is inserted into the {general_term}-everything table successfully.')