# -*- coding: utf-8 -*-
from twibot_utils.TwiAuth import TwiAuth
from bots.TwiMorph import TwiMorph


def main():
        auth = TwiAuth()
        auth.read_json()
        # 	# auth.get_authorization()
        # 	# auth.get_access_token_and_secret()
        auth.get_authorization()
        # auth.data_write_json()
        # bot = Twibot(auth.api)
        # bot.do_single_tweet('tweeet')
        bot = TwiMorph(auth.api, logging=True)
        # bot = TwiMorph(auth.api)
        # bot.get_all_tweets('Kn1fecult')
        # bot.write_json()
        bot.read_to_list()
        # print(bot.source_tweets[0:50])
        bot.tweet()


if __name__ == '__main__':
    main()
