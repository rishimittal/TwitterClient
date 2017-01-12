#!/usr/bin/env python
from Tweet import Tweets

if __name__ == '__main__':
    t = Tweets('#custserv', 20, 1000000)
    t.get_tweets()
