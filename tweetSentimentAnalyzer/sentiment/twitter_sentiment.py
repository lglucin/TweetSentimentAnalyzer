#!/usr/bin/python
import graderUtil
import tweepy
import util
import time
from util import *

grader = graderUtil.Grader()
submission = grader.load('submission')


def get_tweets(hashtag):
    consumer_key='80Qil7rZbocKek1ndNSbf61Ls'
    consumer_secret='S7uhK6K0ayd2Yjng6CuhucvdHdwgd8GcTAGz62KmGikSCdhoyS'
    access_token_key='3132985164-L3CZZlRkhZkKsHNcIzJ8RhILOGju3gjbxmBgeWm'
    access_token_secret='ypDDFiuQIjCIH1e6SeDnE3grH5xT9juujJJG7DqDmKfLe'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    tweets = api.search('#' + hashtag, count = 100, lang = 'en')
    examples = []
    for tweet in tweets:
        examples.append(tweet.retweeted_status.text.encode('utf-8').strip() if hasattr(tweet, 'retweeted_status') else tweet.text.encode('utf-8').strip())
    examples = list(set(examples))
    removed_examples = []
    for i in examples:
        removed_examples.append((i, 1))
    return removed_examples


