import os
from googleapiclient.discovery import build
from dotenv import load_dotenv

class Googs:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('api')
        self.cx = os.getenv('cse')

    def search(self, topic:str, limit:int):
        if limit > 10 and limit < 1:
            raise ValueError("Limit is 1 to 10")

        resource = build('customsearch','v1',developerKey=self.api_key).cse()
        result = resource.list(q=f"Essay about {topic}", cx=self.cx).execute()

        links = []
        for i in range(limit):
            links.append(result['items'][i]['link'])
        return links