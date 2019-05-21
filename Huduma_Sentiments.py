__author__ = "Kevin"

import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt


def percentage(part, whole):
    return 100 * float(part) / float(whole)


# Authentication
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

# Initialize
positive = 0
negative = 0
neutral = 0
polarity = 0

# .Sentiment returns a polarity between -1.0(Completely Negative) and 1.0(Completely positve)
# If 0 its negative, >0 its positive, <0 its negative
# A value of 1 is then added to the corresponding sentiment

for tweet in tweets:
    # print(tweet.text)
    analysis = TextBlob(tweet.text)
    # print(analysis.sentiment)
    polarity += analysis.sentiment.polarity

    if analysis.sentiment.polarity == 0:
        neutral += 1
    elif analysis.sentiment.polarity < 0.00:
        negative += 1
    elif analysis.sentiment.polarity > 0.00:
        positive += 1

# Calculate percentage using def percentage
positive = percentage(positive, no_of_search_terms)
negative = percentage(negative, no_of_search_terms)
neutral = percentage(neutral, no_of_search_terms)

# Format to 2dp
positive = format(positive, '.2f')
neutral = format(neutral, '.2f')
negative = format(negative, '.2f')

# Plotting
labels = ['Positive[' + str(positive) + '%]', 'Neutral[' + str(neutral) + '%]', 'Negative[' + str(negative) + '%]']
sizes = [positive, neutral, negative]
colors = ['yellowgreen', 'gold', 'red']

patches, texts = plt.pie(sizes, colors=colors, startangle=90)
plt.legend(patches, labels, loc="best")
plt.title("Public perception of " + search_term + " by analyzing " + str(no_of_search_terms) + " tweets.")
plt.axis('equal')
plt.tight_layout()
plt.show()
