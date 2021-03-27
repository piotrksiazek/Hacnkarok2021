import requests
import json
from datetime import datetime


class NewsApi:
    def __init__(self):
        self.api_key = '26db25030c8a456aa45c9577b89bfd4b'

    def get_date(self, days):
        today = str(datetime.today()).split()[0]
        yesterday = today[:-2] + str(int(today[-2:]) - days)
        return [yesterday, today]

    def get_headlines(self):
        response = json.loads(requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}').content)
        articles = response['articles']
        titles = [article['title'] for article in articles]
        return titles

    def get_about(self, topic):
        date = self.get_date(7)
        yesterday = date[0]
        today = date[1]
        response = json.loads(
            requests.get(f'https://newsapi.org/v2/top-headlines?q={topic}&from={yesterday}&to={today}&sortBy=popularity&apiKey={self.api_key}').content)
        titles = [article['title'] for article in response['articles']]
        return titles
