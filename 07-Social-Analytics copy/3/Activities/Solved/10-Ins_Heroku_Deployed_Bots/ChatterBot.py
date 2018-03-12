# Dependencies
import tweepy
import json
import time

# Twitter API Keys
import os
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")


# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# Create a function that tweets
def TweetOut(tweet_number):
    api.update_status(f"This is Tweet #{tweet_number}!")


# Create a function that calls the TweetOut function every minute
counter = 0

# Infinitely loop
interval = 15
t_end = time.time() + interval * 5
while(time.time() < t_end):
    # Call the TweetQuotes function and specify the tweet number
    TweetOut(counter)
    time.sleep(interval)
    counter = counter + 1
