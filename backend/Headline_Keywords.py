import json
import openai
from Database import DB_Operation
import os
from dotenv import load_dotenv

class Headline_Keywords():
    def __init__(self, openai_api, id='1'):        
        if type(openai_api) != str:
            raise TypeError(f'The input openai_api: {openai_api} should be string type.')
        self.openai_api = openai_api
        if type(id) != str:
            raise TypeError(f'The input id: {id} should be string type.')
        self.id = id
        self.db_operation = DB_Operation()

    def call_chatgpt(self):
        for category in ['business']:
            print(f'Start fetching data for {category}')
            response = self.db_operation.read('top_news', self.id)
            #Fetch the headlines
            #Preprocess the headlines into the format for ChatGPT
            data = response['Item']['articles']
            headlines_lst = []
            for list_dict in data:
                dict1 = {}
                dict1['description'] = list_dict['description']
                dict1['title'] = list_dict['title']
                dict1['content'] = list_dict['content']
                headlines_lst.append(dict1)
            headlines_lst = str(headlines_lst)

            # Set up your API key
            #Initiate ChatGPT API
            openai.api_key = self.openai_api

            response = openai.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": """
                        You are the agent that generate JSON. You always return just the JSON as follows with no additional description or context.
                        You have a list of headlines including title, url, description and brief content in JSON format as input.
                        Provide the key words for the headline as follows:
                        {'headlines': [
                            {
                                "title": "title_1",
                                "keywords": ["keyword_1", "keyword_2"...]
                            },
                            {
                                "title": "title_2",
                                "keywords": ["keyword_1", "keyword_2"...]
                            }
                        ]}
                    """},
                {"role": "user", "content": headlines_lst}
            ],
            response_format={"type": "json_object"}
            )

            # Parse ChatGPT JSON output into a Python dictionary
            parsed_json = json.loads(response.choices[0].message.content)
            
            ### Include the keywords by ChatGPT into the original headlines table
            response = self.db_operation.read('top_news', self.id)
            headlines_news = response['Item']
            headline_keywords = {'totalResults':headlines_news['totalResults'], 'articles':[]}
            for headline in headlines_news['articles']:
                try:
                    for chatgpt_headline in parsed_json['headlines']:
                        if chatgpt_headline['title'] == headline['title']:
                            headline['keywords'] = chatgpt_headline['keywords']
                            headline_keywords['articles'].append(headline)
                            break
                except Exception as e:
                    print("An error occurred:", e)
                    break
            headline_keywords['id'] = self.id
            #access the table in dynamoDB. write the data to the database
            self.db_operation.write(f'top_news', headline_keywords)

if __name__ == '__main__':
    # Load the environment variables for credentials
    load_dotenv()
    openai_api = os.getenv('openai_api_key')
    print('openai_api: ', openai_api)
    headline = Headline_Keywords(openai_api, id='1')
    headline.call_chatgpt()

            