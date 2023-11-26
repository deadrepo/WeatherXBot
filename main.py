#!/usr/bin/env python
# -*- coding: utf-8 -*-


##                         ##   ######                     #####
### ##   #####     #####   ### ##  #######   #####    #####   #######   #####
#### ##  #######   ######  #### ##  ##       #######  #######  ##   ##  #######
##   ##  ##  ###  ###  ##  ##   ##  ######   ##   ##  ##  ###  ## ####  ##   ##
##   ##  ##  ##   ##   ##  ##   ##  ##   ##  ##       ##  ##   ## ###   ##   ##
######   ####     #######  ######   #######  ##       ####     ##       #######
#####    #####    #####    #####    #####   ##        #####   ##        #####


# WeatherXBot Project By Ikmal 2023


from flask import Flask
import requests
import tweepy, time, sys, urllib, json

app = Flask(__name__)


@app.route("/")
def index():
    # config
    api_key = ""
    api_secret = ""
    bearer_token = r""
    access_token = ""
    access_token_secret = ""

    client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    url = 'https://api.data.gov.my/weather/forecast/?contains=Shah%20Alam@location__location_name'
    urlquotes = 'https://api.quotable.io/quotes/random'

    response = requests.get(url)
    response1 = requests.get(urlquotes)

    storage = response.json()
    storage1 = response1.json()

    print(type(storage))
    print(type(storage1))

    print(storage[6]['date'])
    print(storage[6]['location']['location_name'])
    print(storage[6]['morning_forecast'])
    print(storage[6]['afternoon_forecast'])
    print(storage[6]['night_forecast'])

    print(storage1[0]['content'])
    print(storage1[0]['author'])

    date = storage[6]['date']
    location = storage[6]['location']['location_name']
    morning = storage[6]['morning_forecast']
    afternoon = storage[6]['afternoon_forecast']
    night = storage[6]['night_forecast']

    quotes = storage1[0]['content'] + "\nby " + storage1[0]['author']

    client.create_tweet(
        text=location + " Weather Forecast as in " + date + " →\n\n🌅 Morning: " + morning + "\n🌆 Afternoon: " + afternoon + "\n🌃 Night: " + night + "\n\n" + quotes)

    return "<p>Track Tweeted !</p>"


if __name__ == "__main__":
    app.run()