# TwitterClient

TwitterClient is python client used for retrieving tweets based on two conditions:

1. hashtags
2. Tweets that are retweeted more than once


Requirements

1. Python 2+
2. Tweepy Library [link](http://docs.tweepy.org/en/v3.5.0/)

Why Tweepy?

Tweepy is amazing package in python, which is very good in accessing Twitter API's, Some of the features of Tweepy used in this Client are:

1. Auto Wait(sleep) if API rate limit reached, giving you endless access to Tweets.
2. AppAuthHandler(App-only Auth which gives you higher rate limits)


Setup Instructions

1. git clone https://github.com/rishimittal/TwitterClient
2. cd TwitterClient
3. virtualenv venv ( sudo apt-get install virtualenv )
4. source venv/bin/activate
5. pip install -r requirements.txt
6. cp settings.py.sample src/settings.py
7. Update the settings.py(using [Instructions](https://dev.twitter.com/resources))
8. python src/main.py
