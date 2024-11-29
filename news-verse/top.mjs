// Import necessary AWS SDK modules
import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";
import { unmarshall } from "@aws-sdk/util-dynamodb";
// Create DynamoDB client
const client = new DynamoDBClient({ region: "us-east-1" }); // No explicit credentials; use default provider chain
// Define and export the Lambda handler function
export async function handler(event) {
    const tableName = "top_news"; // Replace with your table name
    const key = {
        id: { S: event.id || "1" }, // Use the 'id' from the event object, default to "1"
    };
    try {
        // Construct DynamoDB GetItemCommand parameters
        const params = {
            TableName: tableName,
            Key: key, // Must match the schema of the table's primary key
        };
        // Execute the GetItemCommand
        const command = new GetItemCommand(params);
        const response = await client.send(command);
        // Unmarshall the item to convert it to a plain object
        if (response.Item) {
            const item = unmarshall(response.Item);
            console.log("Item unmarshalled successfully:", item);
            return {
                statusCode: 200,
                body: JSON.stringify(item),
            };
        } else {
            console.log("No item found.");
            return {
                statusCode: 404,
                body: JSON.stringify({ message: "No item found." }),
            };
        }
    } catch (error) {
        console.error("Error retrieving item:", error);
        return {
            statusCode: 500,
            body: JSON.stringify({ message: "Failed to retrieve item.", error: error.message }),
        };
    }
}