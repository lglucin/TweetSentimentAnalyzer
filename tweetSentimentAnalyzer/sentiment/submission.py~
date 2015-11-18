#!/usr/bin/python

import random
import collections
import math
import sys
from collections import Counter
from util import *

############################################################
# Problem 3: binary classification
############################################################

############################################################
# Problem 3a: feature extraction

def extractWordFeatures(x):
    """
    Extract word features for a string x. Words are delimited by
    whitespace characters only.
    @param string x: 
    @return dict: feature vector representation of x.
    Example: "I am what I am" --> {'I': 2, 'am': 2, 'what': 1}
    """
    # BEGIN_YOUR_CODE (around 5 lines of code expected)
    temp = x.split()
    features = {i:0 for i in temp}
    for i in temp:
        features[i] += 1
    return features
    # END_YOUR_CODE

############################################################
# Problem 3b: stochastic gradient descent

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
     # trainError = evaluatePredictor(trainExamples, lambda(x): (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
     # devError = evaluatePredictor(testExamples, lambda(x): (1 if dotProduct(featureExtractor(x), weights) >= 0 else -1))
     # print "Official: train error = %s, dev error = %s" % (trainError, devError)
    # END_YOUR_CODE
    return weights

############################################################
# Problem 3c: generate test case

def generateDataset(numExamples, weights):
    '''
    Return a set of examples (phi(x), y) randomly which are classified correctly by
    |weights|.
    '''
    random.seed(42)
    # Return a single example (phi(x), y).
    # phi(x) should be a dict whose keys are a subset of the keys in weights
    # and values can be anything (randomize!) with a nonzero score under the given weight vector.
    # y should be 1 or -1 as classified by the weight vector.
    def generateExample():
        # BEGIN_YOUR_CODE (around 2 lines of code expected)
        keys = weights.keys()
        phi = {i: (random.random()-0.5) for i in random.sample(keys, random.randint(0, len(keys)))}
        y = 0
        if dotProduct(phi, weights) > 0:
            y = 1
        elif dotProduct(phi, weights) < 0:
            y = -1
        else:
            return generateExample()
        return (phi, y)
    return [generateExample() for _ in range(numExamples)]

############################################################
# Problem 3f: character features

def extractCharacterFeatures(n):
    '''
    Return a function that takes a string |x| and returns a sparse feature
    vector consisting of all n-grams of |x| without spaces.
    EXAMPLE: (n = 3) "I like tacos" --> {'Ili': 1, 'lik': 1, 'ike': 1, ...
    You may assume that n >= 1.
    '''

    def extract(x):
        # BEGIN_YOUR_CODE (around 10 lines of code expected)
        word = x.replace(" ", "")
        features = {}
        if len(word) >= n:
            for i in xrange(0, len(word)-n+1):
                features[word[i:i+n]] = 0.0
        if len(word) >= n:
            for i in xrange(0, len(word)-n+1):
                features[word[i:i+n]] += 1.0
        return features
        # END_YOUR_CODE
    return extract

############################################################
# Problem 3h: extra credit features

def extractExtraCreditFeatures(x):
    # BEGIN_YOUR_CODE (around 1 line of code expected)
    raise Exception("Not implemented yet")
    # END_YOUR_CODE

############################################################
# Problem 4: k-means
############################################################


def kmeans(examples, K, maxIters):
    '''
    examples: list of examples, each example is a string-to-double dict representing a sparse vector.
    K: number of desired clusters. Assume that 0 < K <= |examples|.
    maxIters: maximum number of iterations to run for (you should terminate early if the algorithm converges).
    Return: (length K list of cluster centroids,
            list of assignments, (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
            final reconstruction loss)
    '''
    # BEGIN_YOUR_CODE (around 35 lines of code expected)
    converged = False
    k_list = random.sample(examples, K)
    assignments = [0]*len(examples)
    while not converged and maxIters > 0:
        done = K
        for a, i in enumerate(examples):
            min = -1
            for b, j in enumerate(k_list):
                if min == -1:
                    min = ((j[0] - i[0])**2 + (j[1] - i[1])**2)**0.5
                    assignments[a] = b
                temp = ((j[0] - i[0])**2 + (j[1] - i[1])**2)**0.5
                if temp < min:
                    min = temp
                    assignments[a] = b
        for k in xrange(0, K):
            x = 0
            y = 0
            num_in_k = 0
            for i, v in enumerate(assignments):
                if v == k:
                    num_in_k += 1
                    x += examples[i][0]
                    y += examples[i][1]
            if num_in_k != 0:
                if k_list[k] != {0: x*1.0/num_in_k, 1: y*1.0/num_in_k}:
                    k_list[k] = {0: x*1.0/num_in_k, 1: y*1.0/num_in_k}
                else:
                    done -= 1
        if done == 0:
            converged = True
        maxIters -= 1
    FCL = 0
    for a, i in enumerate(examples):
        k = assignments[a]
        j = k_list[k]
        FCL += (i[0] - j[0])**2 + (i[1] - j[1])**2
    return k_list, assignments, FCL
    # END_YOUR_CODE
