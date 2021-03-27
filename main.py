from flask import Flask, jsonify
from scraper import Scraper
from newsapi import NewsApi
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
            'healthcare': news_api.get_about('healthcare'),
            'pandemic': news_api.get_about('pandemic')
        },
        'environment_climate_change': {
            'environment': news_api.get_about('environment'),
            'climate_change': news_api.get_about('climate')
        },
        'government_society_finance': {
            'government': news_api.get_about('government'),
            'society': news_api.get_about('society'),
            'finance': news_api.get_about('finance')
        }
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
