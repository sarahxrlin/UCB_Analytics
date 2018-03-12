# Dependencies
import numpy as np
import pandas as pd
import tweepy
import time
import json
import os
# Twitter API Keys
"""
consumer_key = "CQiz5ULMyK8tW3JnyYrRue9Gf"
consumer_secret = "PapdfPnf9IyKfuFvkRvt7yC640Itn38O0qkBoTLKGYB9vmp2Ry"
access_token = "846154323700715520-5dJ8EhhUSRuWzkVb2U0GxIbj4cTuDF6"
access_token_secret = "jDzpohYQYFuDyd9qK9bWQ419Y0nTCFvmMFZYUipQVFs0e"
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
conversation_partner = "@BattleBot_2"

# Send opening message to conversation partner
api.update_status("Hey %s! What's up?" % conversation_partner)

# Response Lines
response_lines = [
    "@BattleBot_2 How are you?",
    "@BattleBot_2 are you having fun?"
    "@BattleBot_2 are you bored?",
    "@BattleBot_2 are you cardboard?",
    "@BattleBot_2 what a great conversation!"
    ]


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


# Set timer to run every 15 seconds
counter = 0
interval = 15  # seconds
for i in range(5):
    time.sleep(interval)
    Converse(i)
