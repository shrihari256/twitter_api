from http import client
import tweepy
import configparser
import os
import pandas as pd
import time


# read all credentials from config file
config = configparser.ConfigParser()
config.read('Twitter API/config.ini')
print('successfully read config file')

api_key             = config['twitter']['api_key']
api_secret          = config['twitter']['api_secret']

access_token        = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

bearer_token        = r"AAAAAAAAAAAAAAAAAAAAADL6lAEAAAAAyjVNm%2FOa6z1s2IKm1ew%2FimRNybM%3Dr8fVGMeKRaN7lrLP7noJvYUiIO7r9uIApLxiNfwziz9Fvdvtns"

# authenticaion
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

keywords =['2023', '#python']



class Listener(tweepy.StreamingClient):
    
    # def __init__(self, tweet_limit = 10):
    #     self.tweet_limit = tweet_limit
    #     self.tweets = []
    #     self.tweet_counter = 1

    tweets = []
    limit = 5
    tweet_counter = 1

    def on_connect(self):
        print('connected')
        return super().on_connect()
    
    def on_tweet(self, tweet):

        if tweet.referenced_tweets == None:
            print(str(self.tweet_counter) +'/' + str(self.limit) + ' tweets \n')
            print(tweet.text + '\n')
            self.tweets.append(tweet)
            print("\033c", end="")
            self.tweet_counter += 1
            # self.tweets.append(tweet.text)
            if self.tweet_counter >= self.limit:
                self.disconnect()
                print('disconnected')

                print(len(self.tweets))
                return False

        time.sleep(0.2)

        return super().on_tweet(tweet)


    def on_status(self, status):
        self.tweets.append(status)

        if self.tweet_counter >= self.limit:
            self.disconnect()
            print('disconnected')
            return False

        # if len(self.tweets) >= self.limit:
        #     self.disconnect()
        #     print('disconnected')

    #     print(status.user.screen_name + ": " + status.text)

    # def on_error(self, status_code):
    #     if status_code == 420:
    #         # returning False in on_error disconnects the stream
    #         return False

stream_tweet    = Listener(bearer_token=bearer_token)


for term in keywords:
    stream_tweet.add_rules(tweepy.StreamRule(term))

stream_tweet.filter(tweet_fields=['referenced_tweets'])


# create a dataframe
columns = ['User', 'Tweet']
data = []


for tweet in stream_tweet.tweets:
    print(dir(tweet))
    # print(tweet.text)
    # data.append([tweet.user.screen_name, tweet.text])

# df = pd.DataFrame(data, columns=columns)

# df.to_csv('tweets.csv', index=False)