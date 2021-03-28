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
    healthcare = news_api.get_about('healthcare', 1)
    healthcare_news = healthcare[0]
    healthcare_imgs = healthcare[1]

    pandemic = news_api.get_about('pandemic', 1)
    pandemic_news = pandemic[0]
    pandemic_imgs = pandemic[1]

    environment = news_api.get_about('environment', 1)
    environment_news = environment[0]
    environment_imgs = environment[1]

    climate_change = news_api.get_about('climate', 1)
    climate_change_news = climate_change[0]
    climate_change_imgs = climate_change[1]

    politics = news_api.get_about('politics', 1)
    politics_news = politics[0]
    politics_imgs = politics[1]

    protests = news_api.get_about('protests', 1)
    protests_news = protests[0]
    protests_imgs = protests[1]

    finance = news_api.get_about('finance', 1)
    finance_news = finance[0]
    finance_imgs = finance[1]

    all_images = [healthcare_imgs, pandemic_imgs, environment_imgs, climate_change_imgs, politics_imgs,
                  protests_imgs, finance_imgs]

    all_images_extended = []
    for image_list in all_images:
        all_images_extended.extend(image_list)

    response = {
        'worldometers': scraper.get_worldometers(),
        'news_api': news_api.get_headlines(),
        'healthcare_pandemic': {
            'healthcare': healthcare_news,
            'pandemic': pandemic_news
        },
        'environment_climate_change': {
            'environment': environment_news,
            'climate_change': climate_change_news
        },
        'politics_protests_finance': {
            'politics': politics_news,
            'protests': protests_news,
            'finance': finance_news
        },
        'image_urls': all_images_extended
    }

    # response = {
    #     'worldometers': scraper.get_worldometers(),
    #     'news_api': news_api.get_headlines(),
    #     'healthcare_pandemic': {
    #         'healthcare': news_api.get_about('healthcare', 0)[0],
    #         'pandemic': news_api.get_about('pandemic', 0)[0]
    #     },
    #     'environment_climate_change': {
    #         'environment': news_api.get_about('environment', 0)[0],
    #         'climate_change': news_api.get_about('climate', 0)[0]
    #     },
    #     'politics_protests_finance': {
    #         'politics': news_api.get_about('politics', 0)[0],
    #         'protests': news_api.get_about('protests', 0)[0],
    #         'finance': news_api.get_about('finance', 0)[0]
    #     }
    # }
    return jsonify(response)



if __name__ == '__main__':
    app.run(debug=True)
