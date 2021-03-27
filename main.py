from flask import Flask, jsonify
from scraper import Scraper
from selenium import webdriver
app = Flask(__name__)
scraper = Scraper()


@app.route('/')
def world_population():
    return jsonify(scraper.get_worldometers())



if __name__ == '__main__':
    app.run(debug=True)
