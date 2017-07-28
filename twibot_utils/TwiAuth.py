# -*- coding: utf-8 -*-
import os
import webbrowser
import json
from tweepy import OAuthHandler, API


class TwiAuth():
    '''

        getting access token and access secret

    '''

    def __init__(self, *argv):
        '''

            if you have acces token and access secret, you may 
            use:
            auth = TwiAuth(access_token, access_secret)

        '''
        self.consumer_key = os.environ.get('consumer_key')
        self.consumer_secret = os.environ.get('consumer_secret')
        self.auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        if argv:
            self.access_token = argv[0]
            self.access_secret = argv[1]

    def get_access_token_and_secret_from_web(self):
        '''

            access token and access secret is getting from
            twitters web authorization

        '''
        webbrowser.open(self.auth.get_authorization_url())
        verifier = input('PIN: ').strip()
        self.auth.get_access_token(verifier)
        print('export user_access_token=' + self.auth.access_token)
        print('export user_access_secret=' + self.auth.access_secret)
        self.access_token = self.auth.access_token
        self.access_secret = self.auth.access_secret

    def get_access_token_and_secret_from_env(self, user='user'):
        '''

            access token and access secret is getting from
            enviroments config file

        '''
        self.access_token = os.environ.get(user + '_access_token')
        self.access_secret = os.environ.get(user + '_access_secret')

    def get_authorization(self):
        '''

            getting example of API for twitter bot

        '''
        auth = OAuthHandler(self.consumer_key, self.consumer_secret)
        auth.set_access_token(self.access_token, self.access_secret)
        self.api = API(auth)

    def data_to_json(self):
        '''

        convert your consumer_key, consumer_secret, access_token,
        access_secret to dictionary

        '''
        self.data = {
            'consumer_key': self.consumer_key,
            'consumer_secret': self.consumer_secret,
            'access_token': self.access_token,
            'access_secret': self.access_secret
        }

    def read_json(self):
        '''

        read consumer_key, consumer_secret, access_token,
        access_secret from json file 

        '''
        self.data = json.load(open('src/credentials.json'))
        self.access_token = self.data['access_token']
        self.access_secret = self.data['access_secret']
        self.consumer_key = self.data['consumer_key']
        self.consumer_secret = self.data['consumer_secret']

    def data_write_to_json(self, filename='credentials.json'):
        '''

        write dictionary to json file with default name
        'credentials.json'

        '''
        self.data_to_json()
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    pass
