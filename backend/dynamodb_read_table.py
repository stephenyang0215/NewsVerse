import boto3


dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NewsApi')


response = table.get_item(
        Key={
            'totalResults':7196 
        }
)

item = response['Item']
print(item)
#aws dynamodb scan --table-name LatestMovies