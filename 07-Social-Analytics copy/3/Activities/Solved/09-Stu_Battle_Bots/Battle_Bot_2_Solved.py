# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json
import os

# Twitter API Keys
"""
consumer_key = "fhhgMuH6ihuUkegPFr6XMYyAA"
consumer_secret = "vZTDk62m1G8eG5MbvxQv6g8uPOCiZgDl8SmyRALcVRirf2FArF"
access_token = "846156247636344833-qcMXj1HVov3MQqKL2KzoeBejqIIGcpn"
access_token_secret = "dv0WNpnl8iULbrKaM95PdnwTj5KANMQ9axdXbtqKDH5Zu"
"""
consumer_key = os.getenv('twitter_consumer_key')
consumer_secret = os.getenv('twitter_consumer_secret')
access_token = os.getenv('twitter_access_token')
access_token_secret = os.getenv('twitter_access_token_secret')

# Twitter Credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target Term
conversation_partner = "@e7dud7e"

# Response Lines
response_lines = [
    f"{conversation_partner} Things are going great.",
    f"{conversation_partner} Yes, i think I'm having fun!",
    f"{conversation_partner} I'm a bit bored yet",
    f"{conversation_partner} I'm 50% cardboard yes!",
    (f"{conversation_partner} Yes, this was a very "
     "intellectually stimulating conversation!")]


# Create converse function
def Converse(line_number):

    # Find the latest tweet from conversation_partner
    public_tweets = api.search(conversation_partner,
                               count=1, result_type="recent")
    for tweet in public_tweets["statuses"]:
        print(tweet)

        # Respond to the tweet with one of the response lines
        tweet_id = tweet["id"]
        print(tweet_id)
        print(tweet["text"])
        api.update_status(
            response_lines[line_number],
            in_reply_to_status_id=tweet_id)


# Set timer to run every minute
interval = 15  # seconds
for i in range(5):
    Converse(i)
    time.sleep(interval)
