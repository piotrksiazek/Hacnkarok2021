import requests
import json
from datetime import datetime


class NewsApi:
    def __init__(self):
        self.api_key = '26db25030c8a456aa45c9577b89bfd4b'

    def get_headlines(self):
        response = json.loads(requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}').content)
        articles = response['articles']
        titles = [article['title'] for article in articles]
        return titles

    # def get_about(self, topic):
    #     response = json.loads(
    #         requests.get(f'https://newsapi.org/v2/everything?q={topic}&from=2021-03-26&to=2021-03-26&sortBy=popularity&apiKey={self.api_key}'))
