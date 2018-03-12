# Dependencies
import tweepy
import json

# Twitter API Keys
"""
consumer_key = "J6wsydLJOWwV5UmnwCn7kaYS0"
consumer_secret = "2NQBWDUeXLyu9mPiGzQu0ezoZZGcX9kvM7gKAx0vAHMiDDctm6"
access_token = "839621358724198402-Zbn09URWCRB1wWbS7eJNIonc7olTQW8"
access_token_secret = "rPLdOsRHxnKPa7bHULB9BGeLYD2qYnFSW1CobqKp2klnX"
"""
# Twitter API Keys
consumer_key = "Ed4RNulN1lp7AbOooHa9STCoU"
consumer_secret = "P7cUJlmJZq0VaCY0Jg7COliwQqzK0qYEyUF9Y0idx4ujb3ZlW5"
access_token = "839621358724198402-dzdOsx2WWHrSuBwyNUiqSEnTivHozAZ"
access_token_secret = "dCZ80uNRbFDjxdU2EckmNiSckdoATach6Q8zb7YYYE5ER"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

# Target User
target_user = "warriors"

# Target File
output_file = "SampleWarriors.json"

# Get all tweets from home feed
public_tweets = api.user_timeline(target_user)

# Open Output
with open(output_file, "w") as outfile:
    json.dump(public_tweets, outfile)
