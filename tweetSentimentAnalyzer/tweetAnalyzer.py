#!/usr/bin/python

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
from contextlib import closing
import __init__
import sys
sys.path.insert(0, '/Users/lloydlucin/Documents/Classes/SeniorYear/FallQuarter/CS92SI/finalProject/tweetSentimentAnalyzer/sentiment/')
import tweepy
import util
import time
import submission
from util import *
from twitter_sentiment import get_tweets

# configuration
DATABASE = '/tmp/tweetAnalyzer.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

# test the classifier on a large dataset
trainExamples = readExamples('sentiment/polarity.train')
featureExtractor = submission.extractCharacterFeatures(3)
weights = submission.learnPredictor(trainExamples, None, featureExtractor)
print "Training complete"


@app.route('/', methods=['GET', 'POST'])
@app.route('/?hash_tag=<hash_tag>')
def show_entries(hash_tag=""):

    hash_tag = ""
    result = []
    prediction = ('','')
    value = 0

    if len(request.args) != 0:
        print "Evaluating" + request.args.get('hash_tag')
        hash_tag = request.args.get('hash_tag')
        tweets = get_tweets(hash_tag)
        outputWeights(weights, 'weights')
        
        # result = [(string, 1 or -1) ...]
        result = evaluatePredictor(tweets, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
        
        # prediction = (Number of negative, number of positive)
        prediction = printPrediction(tweets, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))

        print "Result:"
        print result

        print "Prediction:"
        print prediction

        print "Length of result is: " + str(len(result))

        value= (1.0 * prediction[1]-prediction[0] )/ len(result)
        print value

    return render_template('show_entries.html', hash_tag=hash_tag, color=getColor(value), results=result, prediction=prediction, value=value)


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

def getColor(sentiment):
    if sentiment >= -1 and sentiment <= -0.8:
        return '#FF0000';
    elif sentiment >= -0.8 and sentiment <= -0.6: 
        return '#FF3232';
    elif sentiment >= -0.6 and sentiment <= -0.4:
        return '#FF6666';
    elif sentiment >= -0.4 and sentiment <= -0.2: 
        return '#FF9999';
    elif sentiment >= -0.2 and sentiment < 0: 
        return '#FFCCCC';
    elif sentiment >= 0 and sentiment < 0.1: 
        return '#b2b2b2';
    elif sentiment >= 0.1 and sentiment < 0.2:
        return '#8c8c8c';
    elif sentiment >= 0.2 and sentiment < 0.3: 
        return '#666666';
    elif sentiment >= 0.3 and sentiment < 0.34:
        return '#404040';
    elif sentiment >= 0.34 and sentiment < 0.4: 
        return '#004c00';
    elif sentiment >= 0.4 and sentiment < 0.6:
        return '009900';
    elif sentiment >= 0.6 and sentiment < 0.8:
        return '#00cc00';
    elif sentiment >= 0.8 and sentiment <= 1:
        return '#00ff00';
    else:
        return 'error'


# #read_file("tweets.txt")
# # test the classifier on a large dataset
# trainExamples = readExamples('sentiment/polarity.train')
# featureExtractor = submission.extractCharacterFeatures(3)
# weights = submission.learnPredictor(trainExamples, None, featureExtractor)
# done = False
# while not done:
#     hash_tag = input("Which hashtag would you like to evaluate?: ")
#     tweets = get_tweets(hash_tag)
#     outputWeights(weights, 'weights')
#      #result = [(string, 1 or -1) ...]
#     result = evaluatePredictor(tweets, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
#      #prediction = (Number of negative, number of positive)
#     prediction = printPrediction(tweets, lambda(x) : (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
#    # print prediction




if __name__ == '__main__':
    app.run()