// Import necessary AWS SDK modules
const { DynamoDBClient, GetItemCommand } = require("@aws-sdk/client-dynamodb");
const { unmarshall } = require("@aws-sdk/util-dynamodb"); // Import unmarshall function

// Create DynamoDB client
const client = new DynamoDBClient({ 
    region: "us-east-1",
    credentials:{
        accessKeyId:'AKIAUBKFCUWNUSSO7D65',
        secretAccessKey:'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'
    }
}); 
// Function to read an item from a DynamoDB table
const getItem = async (tableName, key) => {
    // Construct the parameters for the GetItemCommand
    const params = {
        TableName: tableName,
        Key: key, // Must match the schema of the table's primary key
    };

    try {
        // Execute the GetItemCommand
        const command = new GetItemCommand(params);
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
        console.error("Error retrieving item:", error);
        throw error;
    }
};

// Example usage
(async () => {
    const tableName = "categories_news"; // Replace with your table name
    const key = {
        id: { S: "1" }, // Replace 'id' with your primary key attribute and value
    };

    try {
        const item = await getItem(tableName, key);
        console.log("Retrieved item:", item);
    } catch (error) {
        console.error("Failed to retrieve item:", error);
    }
})();
  
  
  
  
  
