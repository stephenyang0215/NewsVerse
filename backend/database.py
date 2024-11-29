import boto3

class DB_operation():
    def lambda_handler(self, table):
        response = table.query(
            KeyConditionExpression="#pk= :id",
            ScanIndexForward=False,
            Limit=1, 
            ExpressionAttributeValues={
                ":id": '1'
            }, 
            ExpressionAttributeNames={
                "#pk":"id"
            }
        )
        return response
    
    def read(self, table_name, time):
        dynamodb = boto3.resource('dynamodb')

        table = dynamodb.Table(table_name)
        response = table.get_item(
                Key={
                    'id':'1',
                    'date_time': time
                }
        )
        return response
    
    def write(self, table_name, headline_keywords):
        table = self.dynamodb.Table(table_name)
        table.put_item(
                Item=headline_keywords
        )
        print(f'Data is inserted into the {table_name} table successfully.')

