const { DynamoDBClient, ScanCommand } = require("@aws-sdk/client-dynamodb");

const client = new DynamoDBClient({ region: "us-east-1" }); // Replace with your AWS region
const scanTable = async (tableName) => {
    try {
        const params = { TableName: tableName };
        const command = new ScanCommand(params);
        const result = await client.send(command);

        console.log("Table Scan Result:", JSON.stringify(result.Items, null, 2));
    } catch (error) {
        console.error("Error scanning table:", error);
    }
};

// Example usage
scanTable("categories_news");
