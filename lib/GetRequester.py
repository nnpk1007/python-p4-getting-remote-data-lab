import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)

        return response.content

    def load_json(self):
        json_content = []
        json_data =  json.loads(self.get_response_body())

        for data in json_data:
            json_content.append(data)
        
        return json_content 


custom_url = 'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json'
responses = GetRequester(custom_url)

# Fetch and process data using the instance
json_content = responses.load_json()

print(json_content)