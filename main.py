from flask import Flask, jsonify
from scraper import Scraper
from newsapi import NewsApi
from picture import pixelate
from selenium import webdriver
app = Flask(__name__)
scraper = Scraper()
news_api = NewsApi()


@app.route('/')
def world_population():
    response = {
        'worldometers': scraper.get_worldometers(),
        'news_api': news_api.get_headlines(),
        'healthcare_pandemic': {
            'healthcare': news_api.get_about('healthcare', 0)[0],
            'pandemic': news_api.get_about('pandemic', 0)[0]
        },
        'environment_climate_change': {
            'environment': news_api.get_about('environment', 0)[0],
            'climate_change': news_api.get_about('climate', 0)[0]
        },
        'politics_protests_finance': {
            'politics': news_api.get_about('politics', 0)[0],
            'protests': news_api.get_about('protests', 0)[0],
            'finance': news_api.get_about('finance', 0)[0]
        },
        'picture_urls': news_api.get_about('politics', 1)[1]
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
