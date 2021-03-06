import requests
import json
from datetime import datetime
from picture import get_image_from_url, pixelate

class NewsApi:
    def __init__(self):
        self.api_key = '43a7e9fbcf9345c7bf1ffb42fd952456'

    def get_date(self, days):
        today = str(datetime.today()).split()[0]
        yesterday = today[:-2] + str(int(today[-2:]) - days)
        return [yesterday, today]

    def get_headlines(self):
        response = json.loads(requests.get(f'https://newsapi.org/v2/top-headlines?country=us&apiKey={self.api_key}').content)
        articles = response['articles']
        titles = [article['title'] for article in articles]
        return titles

    def get_about(self, topic, with_pictures):
        date = self.get_date(7)
        yesterday = date[0]
        today = date[1]
        response = json.loads(
            requests.get(f'https://newsapi.org/v2/top-headlines?q={topic}&from={yesterday}&to={today}&sortBy=popularity&apiKey={self.api_key}').content)
        titles = []
        picture_urls = []
        processed = []
        for article in response['articles']:
            titles.append(article['title'])
            picture_urls.append(article['urlToImage'])

        if with_pictures:
            for i, url in enumerate(picture_urls):
                if url:
                    try:
                        name = get_image_from_url(url, i)
                        pixelate(name, f'static/{name}', 5)
                        processed.append(f'https://tarotscraper.herokuapp.com/static/{i}.png')
                    except requests.exceptions.MissingSchema:
                        continue
                    except ValueError:
                        continue
            
        titles = [article['title'] for article in response['articles']]
        return titles, processed
