# Setting up tweepy authentication
from tweepy import OAuthHandler
from tweepy import API

# Consumer key authentication
auth = OAuthHandler(consumer_key, consumer_secret)

# Access key authentication
auth.set_access_token(access_token, access_token_secret)

# Set up the API with the authentication handler
api  = API(auth)

# Collecting data on keywords
from tweepy import Stream

# Set up words to track
keywords_to_track = ['#rstats','#python']

# Instantiate the SListener object 
listen = SListener(api)

# Instantiate the Stream object
stream = Stream(auth, listen)

# Begin collecting data
stream.filter(track = keywords_to_track)

# Loading and accessing tweets
# Load JSON
import json

# Convert from JSON to Python object
tweet = json.loads(tweet_json)

# Print tweet text
print(tweet['text'])

# Print tweet id
print(tweet['id'])

# Accessing user data
# Print user handle
print(tweet['user']['screen_name'])

# Print user follower count
print(tweet['user']['followers_count'])

# Print user location
print(tweet['user']['location'])

# Print user description
print(tweet['user']['description'])

# Accessing retweet data
# Print the text of the tweet
print(rt['text'])

# Print the text of tweet which has been retweeted
print(rt['retweeted_status']['text'])

# Print the user handle of the tweet
print(rt['user']['screen_name'])

# Print the user handle of the tweet which has been retweeted
print(rt['retweeted_status']['user']['screen_name'])
