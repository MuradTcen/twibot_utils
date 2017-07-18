# -*- coding: utf-8 -*-
import os
import webbrowser
import json
from tweepy import OAuthHandler, API


class TwiAuth():

    def __init__(self, *argv):
        self.consumer_key = os.environ.get('consumer_key')
        self.consumer_secret = os.environ.get('consumer_secret')
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        if argv:
            self.access_token = argv[0]
            self.access_secret = argv[1]

    def get_access_token_and_secret(self):
        webbrowser.open(self.auth.get_authorization_url())
        verifier = input('PIN: ').strip()
        self.auth.get_access_token(verifier)
        print('export user_access_token=' + self.auth.access_token)
        print('export user_access_secret=' + self.auth.access_secret)
        self.access_token = self.auth.access_token
        self.access_secret = self.auth.access_secret

    def get_authorization(self):
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = API(auth)

    def data_to_json(self):
        self.data = {
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret,
            'access_token': self.access_token,
            'access_secret': self.access_secret
        }

    def read_json(self):
        self.data = json.load(open('src/credentials.json'))
        self.access_token = self.data['access_token']
        self.access_secret = self.data['access_secret']
        self.consumer_key = self.data['consumer_key']
        self.consumer_secret = self.data['consumer_secret']

    def data_write_json(self):
        self.data_to_json()
        with open('credentials.json', 'w') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    pass
