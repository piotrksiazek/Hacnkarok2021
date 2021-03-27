import requests
import json

class NewsApi:
    def __init__(self):
        self.api_key = '26db25030c8a456aa45c9577b89bfd4b'

    def get_headlines(self):
        response = json.loads(requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}').content)
        articles = response['articles']
        titles = [article['title'] for article in articles]
        return titles
