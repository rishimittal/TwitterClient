# TwitterClient

TwitterClient is python client used for retrieving tweets based on two conditions:

1. hashtags
2. Tweets that are retweeted more than once


Requirements

1. Python 2+
2. Tweepy Library [link](http://docs.tweepy.org/en/v3.5.0/)

Setup Instructions

1. git clone https://github.com/rishimittal/TwitterClient
2. cd TwitterClient
3. virtualenv venv ( sudo apt-get install virtualenv )
4. source venv/bin/activate
5. pip install -r requirements.txt
6. cp settings.py.sample src/settings.py
7. Update the settings.py(using Instructions)
8. python src/main.py
