#!/usr/bin/env python
from Tweet import Tweets

# Executable
if __name__ == '__main__':
    t = Tweets('#custserv', 20, 1000000)
    t.get_tweets()
