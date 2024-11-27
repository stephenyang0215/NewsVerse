// Import necessary AWS SDK modules
const { DynamoDBClient, QueryCommand } = require("@aws-sdk/client-dynamodb");
const { unmarshall } = require("@aws-sdk/util-dynamodb"); // Import unmarshall function

// Create DynamoDB client
const client = new DynamoDBClient({ region: "us-east-1" }); // Replace with your desired region

// Function to query items from a DynamoDB table
const queryByAttribute = async (tableName, indexName, partitionKey, attributeName, attributeValue) => {
    // Construct the parameters for the QueryCommand
    const params = {
        TableName: tableName,
        IndexName: indexName, // Specify the secondary index if querying a non-key attribute
        KeyConditionExpression: "#pk = :pkValue",
        //FilterExpression: "#attr = :attrValue",
        FilterExpression: `contains(#attr , :attrValue)`,
        ExpressionAttributeNames: {
            "#pk": "id", // Replace with your partition key name
            "#attr": attributeName,
        },
        ExpressionAttributeValues: {
            ":pkValue": { S: partitionKey }, // Replace `S` with `N` or `B` if your partition key is a number or binary
            ":attrValue": { S: attributeValue }, // Replace `S` with appropriate type
        },
          
    };

    try {
        // Execute the QueryCommand
        const command = new QueryCommand(params);
        const response = await client.send(command);

        // Unmarshall the item to convert it to a plain object
        if (response.Item) {
            const item = unmarshall(response.Item);
            console.log("Item unmarshalled successfully:", item);
            return item;
        } else {
            console.log("No item found.");
            return null;
        }
    } catch (error) {
        console.error("Error querying items:", error);
        throw error;
    }
};

// Example usage
(async () => {
    const tableName = "categories_news"; // Replace with your table name
    const indexName = "id-index"; // Replace with your index name (for non-key attributes)
    const partitionKey = "1"; // Replace with a valid partition key value
    const attributeName = "business.item.news_sources.keywords"; // Replace with the attribute name
    const attributeValue = "Elon Musk"; // Replace with the attribute value

    try {
        const items = await queryByAttribute(tableName, indexName, partitionKey, attributeName, attributeValue);
        console.log("Queried items:", items);
    } catch (error) {
        console.error("Failed to query items:", error);
    }
})();
