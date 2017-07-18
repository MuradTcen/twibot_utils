# -*- coding: utf-8 -*-
from pymorphy2 import MorphAnalyzer
from twitterbot_utils.Tweet import Tweet
from twitterbot_utils.Twibot import Twibot
from random import choice
import re


class TwiMorph(Twibot):

	def __init__(self, api, template='%s - признак градиентного спуска', word='', logging=False):
		super().__init__(api, logging)
		self.template = template
		self.word = word

	def get_random_string_from_source(self):
		self.random_string = choice(self.source_tweets)

	def get_noun_from_string(self):
		def get_if_noun(word):
			print(word)
			w = MorphAnalyzer().parse(word)[0]
			print(w.tag)
			if 'NOUN' in w.tag:
				return w.normal_form

		self.use_only_russian_words_in_string()
		words = self.random_string.strip().split()
		words = list(map(get_if_noun,words))
		print(words)
		words = [word for word in words if word]
		print(words)
		print(len(words))
		while len(words) == 0:
			print('1')
			self.get_random_string_from_source()
			self.use_only_russian_words_in_string()
			self.get_noun_from_string()
		self.word = choice(words)

	def make_tweet(self):
		self.tweet = Tweet(self.template % self.word)

	def use_only_russian_words_in_string(self):
		self.random_string = ' '.join(re.findall('[А-Яа-я]+', self.random_string))

	def tweet(self):
		self.get_random_string_from_source()
		self.get_noun_from_string()
		self.make_tweet()
		self.do_single_tweet(self.tweet.text)
		if self.logging: print(self.tweet.text)

