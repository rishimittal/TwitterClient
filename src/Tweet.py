#!/usr/bin/env python
import sys
import json
import tweepy
from settings import *


class Tweets:

    search_query = ''
    max_tweets = 0
    qry_tweet_count = 0

    # Constructor
    def __init__(self, search_query, qry_tweet_count, max_tweets):
        print 'Initiating Tweets Fetcher.....!'
        self.search_query = search_query
        self.qry_tweet_count = qry_tweet_count
        self.max_tweets = max_tweets

    # Calling tweets to receive the tweets
    def get_tweets(self):
        # lower bound (tweet Id)
        old_id = None
        # Upper bound (tweet Id)
        max_id = -1L
        tweet_count = 0
        # Using AppAuthHandler, giving higher rate limits
        auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        # Using wait_on_rate_limit & wait_on_rate_limit_notify notifies
        # tweepy api, to auto wait(sleep) when it hits rate limit
        api = tweepy.API(auth, wait_on_rate_limit=True,
        				   wait_on_rate_limit_notify=True)
        # Exit: If authentication is not valid
        if (not api):
            print ("Incorrect Authentication")
            sys.exit(-1)

        # logic to keep on polling and fetching the results, between the lower bound(old_id)
        # upper bound(max_id)
        while tweet_count < self.max_tweets:
            try:
                if(max_id <= 0):
                    if not old_id:
                        new_tweets = api.search(q=self.search_query,
                                                count=self.qry_tweet_count)
                    else:
                        new_tweets = api.search(q=self.search_query,
                                                count=self.qry_tweet_count,
                                                since_id=old_id)
                else:
                    if not old_id:
                        new_tweets = api.search(q=self.search_query,
                                                count=self.qry_tweet_count,
                                                max_id=str(max_id - 1))
                    else:
                        new_tweets = api.search(q=self.search_query,
                                                count=self.qry_tweet_count,
                                                max_id=str(max_id - 1),
                                                since_id=old_id)
                if not new_tweets:
                    print("End of Result: No more tweets found")
                    break
                self.filter_tweets(new_tweets)
                print 'Tweets Fetched: ' + str(len(new_tweets))
                # Updating the max_id
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print("Exception Found : " + str(e))
                break

    # Filter the Tweets with Conditions
    def filter_tweets(self, tweets):
        filter_hashtag = self.search_query[1:]
        tweet_list = []
        for tweet in tweets:
            tweet_json = tweet._json
            # a. Filter tweets based on #custserv(case-insensitive) tag
            hashtag_filter = False
            hashtags = tweet_json['entities']['hashtags']
            for tags in hashtags:
                if tags['text'].lower() == filter_hashtag:
                    hashtag_filter = True

            # b. Filter tweets based on number of retweets
            retweet_filter = False
            if tweet_json['retweet_count'] > 0:
                retweet_filter = True

            if hashtag_filter and retweet_filter:
                tweet_list.append(tweet_json)
        self.return_tweet_results(tweet_list)

    # Return the result in json format
    # field: retweets(Number of retweet count)
    # field: text(Text in Tweet)
    def return_tweet_results(self, tweet_list):
        for tweet in tweet_list:
            tweet_data = {}
            tweet_data['text'] = tweet['text']
            tweet_data['retweets'] = tweet['retweet_count']
            tj = json.dumps(tweet_data)
            parsed = json.loads(tj)
            print json.dumps(parsed, indent=4, sort_keys=True)
        print 'Tweets Fetched after filter : ' + str(len(tweet_list))
