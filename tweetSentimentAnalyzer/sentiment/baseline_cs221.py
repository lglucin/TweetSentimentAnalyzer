__author__ = 'David'
import random
import collections
import math
import sys
from collections import Counter
from util import *

f = open("cs221_baseline_amazon.txt", 'r')

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x:
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    temp = x.split(',')
    return temp[1]
    # END_YOUR_CODE

def extractOpen(x):
    temp = x.split(',')
    return temp[4]

def getMovingAverage(f):
    window = 10
    count = 0
    window = []
    with open(f, 'r') as openfile:
        for line in openfile:
            elif count < 10:
                window.append(float(extractWordFeatures(line)))
                count += 1
            else:
                window.pop(0)
                window.append(float(extractWordFeatures(line)))
    print "Last price is", window[count-1]
    return sum(window) / count, window[count-1]

def getPrediction(movingAvg, f):
    with open(f, 'r') as openfile:
        should = 0
        predict = 0
        for line in openfile:
            open_p = extractOpen(line)
            print "The actual open price is", open_p
            if open_p >= movingAvg[1]:
                print "Should be predicting +1"
                should = 1
            else:
                print "Should be predicting -1"
                should = -1

            if movingAvg[1] >= movingAvg[0]:
                print "Predicing -1"
                predict = -1
            else:
                print "Predicing +1"
                predict = 1
            if predict == should:
                print "Predicted correctly"
            else:
                print "Predicted incorrectly"



print "Amazon"
moving_avg = getMovingAverage("cs221_baseline_amazon.txt")
print "Moving average is", moving_avg[0]
print getPrediction(moving_avg, "cs221_baseline_amazon_predict.txt")

print "Facebook"
moving_avg = getMovingAverage("cs221_baseline_facebook.txt")
print "Moving average is", moving_avg[0]
print getPrediction(moving_avg, "cs221_baseline_facebook_predict.txt")

print "Google"
moving_avg = getMovingAverage("cs221_baseline_google.txt")
print "Moving average is", moving_avg[0]
print getPrediction(moving_avg, "cs221_baseline_google_predict.txt")

print "Microsoft"
moving_avg = getMovingAverage("cs221_baseline_microsoft.txt")
print "Moving average is", moving_avg[0]
print getPrediction(moving_avg, "cs221_baseline_microsoft_predict.txt")

print "Twitter"
moving_avg = getMovingAverage("cs221_baseline_twitter.txt")
print "Moving average is", moving_avg[0]
print getPrediction(moving_avg, "cs221_baseline_twitter_predict.txt")

def learnPredictor(trainExamples, testExamples, featureExtractor):
    '''
    Given |trainExamples| and |testExamples| (each one is a list of (x,y)
    pairs), a |featureExtractor| to apply to x, and the number of iterations to
    train |numIters|, return the weight vector (sparse feature vector) learned.

    You should implement stochastic gradient descent.

    Note: only use the trainExamples for training!
    You should call evaluatePredictor() on both trainExamples and testExamples
    to see how you're doing as you learn after each iteration.
    numIters refers to a variable you need to declare. It is not passed in.
    '''
    weights = {}  # feature => weight
    eta = 0.01
    numIters = 20
    # BEGIN_YOUR_CODE (around 15 lines of code expected)
    for j in xrange(0, numIters):
        for i in trainExamples:
            expected = i[1]
            features = featureExtractor(i[0])
            for a in features:
                if weights.get(a) is None:
                    weights[a] = 0
            margin = dotProduct(weights, features) * expected
            if margin < 1:
                for a in features:
                    weights[a] -= -eta*(features[a])*expected
    # END_YOUR_CODE
    return weights

def evaluatePredictor(examples, predictor):
    '''
    predictor: a function that takes an x and returns a predicted y.
    Given a list of examples (x, y), makes predictions based on |predict| and returns the fraction
    of misclassiied examples.
    '''
    error = 0
    for x, y in examples:
        if predictor(x) != y:
            error += 1
    return 1.0 * error / len(examples)