// Import necessary AWS SDK modules
import { DynamoDBClient, GetItemCommand } from "@aws-sdk/client-dynamodb";
import { unmarshall } from "@aws-sdk/util-dynamodb";

// Create DynamoDB client
const client = new DynamoDBClient({ region: "us-east-1" });

// Define and export the Lambda handler function
export async function handler(event) {
    const tableName = "categories_news";
    const key = {
        id: { S: event.id || "1" }, // Use the 'id' from the event object, default to "1"
    };

    try {
        // Construct DynamoDB GetItemCommand parameters
        const params = {
            TableName: tableName,
            Key: key,
        };

        // Execute the GetItemCommand
        const command = new GetItemCommand(params);
        const response = await client.send(command);

        if (response.Item) {
            const item = unmarshall(response.Item);

            let keywordFrequency = {};

            // Iterate over all categories in the item
            for (const category in item) {
                if (item[category]?.item) {
                    // Iterate over each topic in the category
                    for (const topic of item[category].item) {
                        const uniqueKeywords = new Set();

                        // Iterate over news_sources to collect unique keywords
                        for (const news of topic.news_sources) {
                            if (news.keywords) {
                                news.keywords.forEach(keyword => uniqueKeywords.add(keyword.toLowerCase()));
                            }
                        }

                        // Update keyword frequency
                        uniqueKeywords.forEach(keyword => {
                            if (keywordFrequency[keyword]) {
                                keywordFrequency[keyword] += 1;
                            } else {
                                keywordFrequency[keyword] = 1;
                            }
                        });
                    }
                }
            }

            // Sort keywords by frequency in descending order
            const sortedKeywords = Object.entries(keywordFrequency)
                .sort((a, b) => b[1] - a[1])
                .map(([keyword, frequency]) => ({ keyword, frequency }));

            return {
                statusCode: 200,
                body: JSON.stringify(sortedKeywords),
            };
        } else {
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
