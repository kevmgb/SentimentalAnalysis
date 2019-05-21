# Required libraries

import json
import csv
import tweepy
import re
from textblob import TextBlob



def percentage(part, whole):
    return 100 * float(part) / float(whole)


# Goal: Collect Raw tweets from #Ikokazi
# Inputs: user_key, user_secret, access_token,access_token_secret (for twitter authentication)
# Output: .csv spreadsheet with tweets

# For application authentication

consumer_key = input('Enter Your Consumer Key: ')
consumer_secret = input('Enter Your Consumer Secret: ')
access_token = input('Enter Your Access Token: ')
access_token_secret = input('Enter Your Access Token Secret: ')

# Establish Connection with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

search_term = input("Enter the hashtag that you want to analyze: ")
no_of_search_terms = int(input("Enter the number of search terms: "))

tweets = tweepy.Cursor(api.search, q=search_term).items(no_of_search_terms)

positive = 0
negative = 0
neutral = 0
polarity = 0

for tweet in tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
