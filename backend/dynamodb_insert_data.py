import boto3
dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('Users')

table.put_item(
   Item={
        'username': 'johndoe',
        'last_name': 'Doe',
        'first_name': 'John',
        'age': 25,
        'account_type': 'standard_user',
    }
)

print('Item inserted to the table successfully!')