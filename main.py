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
        'news_api': news_api.get_headlines()
    }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
