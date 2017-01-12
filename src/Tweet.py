#!/usr/bin/env python
import json
import tweepy
from settings import *


class Tweets:

    search_query = ''
    max_tweets = 10000000
    qry_tweet_count = 0

    def __init__(self, search_query, qry_tweet_count):
        print 'Initiating Tweets Fetcher.....!'
        self.search_query = search_query
        self.qry_tweet_count = qry_tweet_count

    def get_tweets(self):
        old_id = None
        max_id = -1L
        tweet_count = 0
        auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True,
        				   wait_on_rate_limit_notify=True)
        if (not api):
            print ("Incorrect Authentication")
            sys.exit(-1)
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
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                print("Exception Found : " + str(e))
                break

    def filter_tweets(self, tweets):
        
        tweet_list = []
        for tweet in tweets:
            tweet_json = tweet._json
            #Filter tweets based on #custserv tag
            hashtag_filter = False
            hashtags = tweet_json['entities']['hashtags']
            for tags in hashtags:
                if tags['text'].lower() == 'custserv':
                    hashtag_filter = True

            #Filter tweets based on number of retweets
            retweet_filter = False
            if tweet_json['retweet_count'] > 0:
                retweet_filter = True

            if hashtag_filter and retweet_filter:
                tweet_list.append(tweet_json)

        self.return_tweet_results(tweet_list)

    def return_tweet_results(self, tweet_list):

        for tweet_json in tweet_list:
            tj = json.dumps(tweet_json)
            parsed = json.loads(tj)
            print json.dumps(parsed, indent=4, sort_keys=True)
        print 'Tweets Fetched after filter : ' + str(len(tweet_list))
