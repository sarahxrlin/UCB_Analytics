# Dependencies
import tweepy
import time
import os


# Twitter API Keys
consumer_key = os.getenv("twitter_consumer_key")
consumer_secret = os.getenv("twitter_consumer_secret")
access_token = os.getenv("twitter_access_token")
access_token_secret = os.getenv("twitter_access_token_secret")


# Twitter credentials
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    
# Quotes to Tweet
quote_list = [("Quote 1: you are guided by "
              "silent love and friendship around you."),
              "Quote 2: the fortune you seek is another cookie.",
              "Quote 3: don't eat the paper"]


# Create function for tweeting
def quote_it_up(quote):

    # Tweet the next quote
    api.update_status(quote)

    # Print success message
    print("Tweeted successfully!")


# Create a loop that tweets one quote per minute until
# all of the quotes have been tweeted
interval = 15  # seconds
for quote in quote_list:
    quote_it_up(quote)
    time.sleep(interval)
