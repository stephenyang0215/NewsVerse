const { DynamoDBClient, QueryCommand } = require("@aws-sdk/client-dynamodb");

// Create DynamoDB client
const client = new DynamoDBClient({ region: "us-east-1" }); // Replace with your AWS region

// Function to query by key and filter by nested attribute
const queryByKeyAndFilter = async (tableName, keyName, keyValue, heightValue) => {
    try {
        const params = {
            TableName: tableName,
            KeyConditionExpression: "#id = :idValue", // Query by primary key
            FilterExpression: "#group.#height = :heightValue", // Filter by nested attribute
            ExpressionAttributeNames: {
                "#id": keyName,
                "#group": "group",
                "#height": "height",
            },
            ExpressionAttributeValues: {
                ":idValue": { S: keyValue },
                ":heightValue": { S: heightValue },
            },
        };

        const command = new QueryCommand(params);
        const result = await client.send(command);
        if (result.Items) {
            result.Items.forEach((item, index) => {
                console.log(`Item ${index + 1}:`, JSON.stringify(item, null, 2));
            });
        } else {
            console.log("No items found.");
        }
        //console.log("Filtered Items:", JSON.stringify(result.Items, null, 2));
        return result.Items;
    } catch (error) {
        console.error("Error querying table:", error);
        throw error;
    }
};

// Example usage
(async () => {
    const tableName = "test"; // Replace with your table name
    const keyName = "id"; // Replace with your primary key name
    const keyValue = "1"; // Replace with the primary key value to query
    const heightValue = "20"; // Replace with the height value to filter by

    try {
        const items = await queryByKeyAndFilter(tableName, keyName, keyValue, heightValue);
        console.log("Retrieved Items:", items);
    } catch (error) {
        console.error("Error:", error);
    }
})();
