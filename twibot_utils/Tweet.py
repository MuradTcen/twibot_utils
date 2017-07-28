# -*- coding: utf-8 -*-
import re


class Tweet():

    '''

    class of tweet
    tweet = Tweet(string)

    '''

    def __init__(self, text):
        self.text = text
        self.check_type()
        self.text = self.text.strip()
        self.convert_special_symbols()
        self.cleaning_tweet_from_links_and_names()
        self.check_length()

    def check_length(self):
        '''

        checking length of text 0 > string > 140


        '''
        if not (len(self.text) > 0 and len(self.text) < 140):
            self.text = ''

    def check_type(self):
        '''

        checking type of string


        '''
        if type(self.text) != str:
            self.text = ''

    def convert_special_symbols(self):
        '''

        converting some special symbols

        
        '''
        self.text = self.text.replace('&gt;', '>').replace('&lt;', '<')

    def cleaning_tweet_from_links_and_names(self):
        '''
        
        removing @names and links


        '''
        pattern_name_start = r'@\w* '
        pattern_name_end = r' @\w*'
        pattern_link_space_begin = r'http\w?:\/\/(www.)?\w*.\w*(\/\w*)* '
        pattern_link_space_end = r' http\w?:\/\/(www.)?\w*.\w*(\/\w*)*'
        tweet = re.sub(pattern_name_start, '', self.text)
        tweet = re.sub(pattern_name_end, '', tweet)
        tweet = re.sub(pattern_link_space_begin, '', tweet)
        result = re.sub(pattern_link_space_end, '', tweet)
        self.text = result


def main():
    pass

if __name__ == '__main__':
    main()
