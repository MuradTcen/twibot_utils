# -*- coding: utf-8 -*-

from tweepy import API
import tweepy
import json

get_text_from_json_tweet = (lambda tweet: tweet._json['text'])


class Twibot(object):

    def __init__(self, api, logging=False):
        self.api = api
        self.api.wait_on_rate_limit = True
        self.logging = logging
        self.file = 'source.json'

    def do_single_tweet(self, tweet):
        try:
            self.api.update_status(tweet)
        # except TweepError as e:
        #     print('tweeperror ' + e)
        except Exception as e:
            print('exception ', e)

    def do_multiple_tweet(self, tweets):
        for tweet in tweets:
            self.do_single_tweet(tweet)
            if self.logging:
                print(tweet)

    def do_wipe(self):
        for tweet in self.api.home_timeline(200)[30:]:
            if tweet.favorite_count + tweet.retweet_count == 0:
                tweet.destroy()

    def get_all_tweets(self, screen_name):
        all_tweets = []
        new_tweets = self.api.user_timeline(screen_name=screen_name, count=200)
        all_tweets.extend(new_tweets)
        oldest = all_tweets[-1].id - 1
        while len(new_tweets) > 0:
            if self.logging: print('getting tweets before %s' % (oldest))
            new_tweets = self.api.user_timeline(
                screen_name=screen_name, count=200, max_id=oldest)
            all_tweets.extend(new_tweets)
            oldest = all_tweets[-1].id - 1
            if self.logging: print('..%s tweets downloaded so far' % (len(all_tweets)))
        # outtweets = [[tweet.id_str, tweet.created_at, tweet.text] for tweet
        # in all_tweets]
        all_tweets = list(map(get_text_from_json_tweet, all_tweets))
        self.source_tweets = all_tweets

    def write_list(self):
        data = self.source_tweets
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def read_to_list(self):
        try:
            data = json.load(open(self.file))
        except:
            data = []
        # data.append(post_dict)
        self.source_tweets = data


def main():
    pass
if __name__ == '__main__':
    main()
