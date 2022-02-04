import tweepy
import json
import time


def main():

    with open('daily-stats.json') as j:
        stats_list = json.loads(j.read())

    

    twitter_auth_keys = {
        "consumer_key"        : "REPLACE_THIS_WITH_YOUR_CONSUMER_KEY",
        "consumer_secret"     : "REPLACE_THIS_WITH_YOUR_CONSUMER_SECRET",
        "access_token"        : "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN",
        "access_token_secret" : "REPLACE_THIS_WITH_YOUR_ACCESS_TOKEN_SECRET"
    }

    auth = tweepy.OAuthHandler(
            twitter_auth_keys['consumer_key'],
            twitter_auth_keys['consumer_secret']
            )
    auth.set_access_token(
            twitter_auth_keys['access_token'],
            twitter_auth_keys['access_token_secret']
            )
    api = tweepy.API(auth)

    today_stats = stats_list[-1]
    today = list(today_stats.keys())[0]

    tweet = f"In last 24 hours ({today})\n New Cases: {today_stats[today]['New Cases']}\nNew Deaths: {today_stats[today]['New Deaths']}"
    post_result = api.update_status(status=tweet)

while True:
    main()
    time.sleep(60*60*24)
