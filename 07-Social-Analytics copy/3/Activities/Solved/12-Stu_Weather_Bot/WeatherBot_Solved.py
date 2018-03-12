# Dependencies
import tweepy
import requests
import time
import datetime
import os

# Twitter API Keys
consumer_key = os.getenv('twitter_consumer_key')
consumer_secret = os.getenv('twitter_consumer_secret')
access_token = os.getenv('twitter_access_token')
access_token_secret = os.getenv('twitter_access_token_secret')

# openweather api key
openweather_api_key = os.getenv('openweather_api_key')
print(f"weather api key {openweather_api_key}")
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that gets the weather in London and Tweets it
def WeatherTweet(city):
    """Tweet the weather."""

    # Construct a Query URL for the OpenWeatherMap
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": "San Francisco",
        "units": "imperial",
        "appid": openweather_api_key
    }

    # Perform the API call to get the weather
    weather_response = requests.get(url, params=params)
    weather_json = weather_response.json()
    print(weather_json)

    # Tweet the weather
    current_datetime = datetime.datetime.now().strftime("%I:%M %p")
    weather = weather_json.get("main").get("temp")

    try:
        api.update_status(f"{city} weather as of "
                          f"{current_datetime}:"
                          f"{weather}")
        print("Tweeted successfully")
    except Exception as e:  # Print success message
        print(e)


# Set timer to 2x
interval = 10  # seconds
city = "San Francisco"
t_end = time.time() + interval * 2
while(time.time() < t_end):
    WeatherTweet(city)
    time.sleep(interval)