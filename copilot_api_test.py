import tweepy
import pandas as pd

# Consumer keys and access tokens, used for OAuth
api_key             = 'c55o9kHfIVZSZcB97sztbmSU7'
api_secret          = "3mKEdJszFVW5LyCv8rv1dAJZ85yUIFwg3gcKV9Zolol7HGfb6P"
bearer_token        = r"AAAAAAAAAAAAAAAAAAAAADL6lAEAAAAAyjVNm%2FOa6z1s2IKm1ew%2FimRNybM%3Dr8fVGMeKRaN7lrLP7noJvYUiIO7r9uIApLxiNfwziz9Fvdvtns"

access_token        = "1614785862113579008-RXyiWQMyJJO1VnjeQoW5qte9ejnQaT"
access_token_secret = "gnSYxOZGg6VbSkumDDwfMC7xLzzbYUu3U5JjOUD2sLurG"

client = tweepy.Client(api_key, api_secret, bearer_token, access_token, access_token_secret)

auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# client.create_tweet(text = "wassup!")
# -------------------------------------------------------------------------------------------------------------------------------------------------

# user tweets
user = 'veritasium'
limit = 300

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

## Twitter api returns only a maximum of 200 tweets at once. Method do pull more:
# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count = 200, tweet_mode='extended').items(limit)

# -------------------------------------------------------------------------------------------------------------------------------------------------
## Search for tweets

keyword = '2022'
# keyword = '#hastag'
# keyword = '@user'
tweets = tweepy.Cursor(api.search_tweets, q=keyword, count = 100, tweet_mode='extended').items(limit)       # max 100 tweets per search request
# -------------------------------------------------------------------------------------------------------------------------------------------------

# create dataframe
columns = ['user','Tweet']
data = []
for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)

