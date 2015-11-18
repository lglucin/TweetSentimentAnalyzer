import tweepy
def get_tweets(hashtag):
    consumer_key='80Qil7rZbocKek1ndNSbf61Ls'
    consumer_secret='S7uhK6K0ayd2Yjng6CuhucvdHdwgd8GcTAGz62KmGikSCdhoyS'
    access_token_key='3132985164-L3CZZlRkhZkKsHNcIzJ8RhILOGju3gjbxmBgeWm'
    access_token_secret='ypDDFiuQIjCIH1e6SeDnE3grH5xT9juujJJG7DqDmKfLe'

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token_key, access_token_secret)

    api = tweepy.API(auth)

    #hashtag = raw_input('Enter a hastag to search: ')

    tweets = api.search('#' + hashtag, count = 100, lang = 'en')
    examples = []
    for i in tweets:
        examples.append((i.strip(), 1))
    return examples

with open(hashtag + '.txt', 'w') as offy:
    for tweet in tweets:
        offy.write(tweet.retweeted_status.text.encode('utf-8').strip() if hasattr(tweet, 'retweeted_status') else tweet.text.encode('utf-8').strip())
        offy.ite('----------')