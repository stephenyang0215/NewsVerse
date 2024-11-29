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
            const keyword = event.keyword?.toLowerCase() || "";

            if (!keyword) {
                return {
                    statusCode: 400,
                    body: JSON.stringify({ message: "Keyword is required for search." }),
                };
            }

            let searchResults = [];

            // Iterate over all categories in the item
            for (const category in item) {
                if (item[category]?.item) {
                    // Iterate over each topic in the category
                    for (const topic of item[category].item) {
                        // Check if the summary or topic contains the keyword
                        if (
                            topic.summary?.toLowerCase().includes(keyword) ||
                            topic.topic?.toLowerCase().includes(keyword)
                        ) {
                            searchResults.push(topic);
                            continue;
                        }

                        // Iterate over news_sources to check if any keywords match
                        const matchingNewsSources = topic.news_sources.filter(news =>
                            news.keywords?.some(kw => kw.toLowerCase().includes(keyword))
                        );

                        if (matchingNewsSources.length > 0) {
                            searchResults.push({
                                topic: topic.topic,
                                summary: topic.summary,
                                news_sources: matchingNewsSources,
                            });
                        }
                    }
                }
            }

            if (searchResults.length > 0) {
                return {
                    statusCode: 200,
                    body: JSON.stringify(searchResults),
                };
            } else {
                return {
                    statusCode: 404,
                    body: JSON.stringify({ message: "No results found for the given keyword." }),
                };
            }
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
