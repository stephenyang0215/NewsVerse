'''
This is the database module which support ACID operations such as read and write for AWS DynamoDB
In order to run the operation, it's required to set up AWS crentials configuration in advance.
'''
import boto3

class DB_operation():
    #read your data from the database
    def read(self, table_name, id):
        #Initiate the dynamodb instance
        dynamodb = boto3.resource('dynamodb')
        #Connect to the table
        table = dynamodb.Table(table_name)
        #Invoke the operation
        response = table.get_item(
                Key={
                    'id':id
                }
        )
        return response
    
    #write your data to the database
    def write(self, table_name, data):
        #Initiate the dynamodb instance
        dynamodb = boto3.resource('dynamodb')
        #Connect to the table
        table = dynamodb.Table(table_name)
        #invoke the operation
        table.put_item(
                Item=data
        )
        print(f'Data is inserted into the {table_name} table successfully.')