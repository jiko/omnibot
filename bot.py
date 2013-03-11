import ConfigParser
import os
import re
from twitter import Twitter, TwitterError
from twitter.oauth import OAuth, read_token_file
from twitter.oauth_dance import oauth_dance
import markovgen
import isopsephy
from random import randint, choice


class Bot:
    def __init__(self, bot, path):
        config = ConfigParser.RawConfigParser()
        config.read(path+bot+"/omni.cfg")
        oauth = config.get(bot, 'oauth')
        consumer_key = config.get(bot, 'consumer_key')
        consumer_secret = config.get(bot, 'consumer_secret')
        oauth_filename = os.environ.get('HOME', '') + os.sep + oauth
        oauth_token, oauth_token_secret = read_token_file(oauth_filename)
        self.handle = config.get(bot, 'handle')
        self.corpus = path + bot + os.sep + config.get(bot, 'corpus')
        self.method = config.get(bot, 'tweet_method')
        self.twitter = Twitter(domain='search.twitter.com')
        self.twitter.uriparts = ()
        self.poster = Twitter(
            auth=OAuth(
                oauth_token,
                oauth_token_secret,
                consumer_key,
                consumer_secret
            ),
            secure=True,
            api_version='1',
            domain='api.twitter.com')

    def generate_text(self):
        text = ""
        with open(self.corpus) as f:
            if self.method == "markov":
                markov = markovgen.Markov(f)
                word_count = randint(6, 18)
                text = markov.generate_markov_text(size=word_count)
            elif self.method == "isopsephy":
                iso = isopsephy.Isopsephia(f.read())
                text = iso.generate_text()
            else:
                lines = [line.strip() for line in f]
                text = choice(lines)[:123]
        return text

    def tweet(self, irtsi=None, at=None):
        status = self.generate_text()
        if at and irtsi:
            status = "@"+at+" "+status
        try:
            self.poster.statuses.update(
                status=status,
                in_reply_to_status_id=irtsi
            )
        except self.TwitterError:
            print "Twitter Error"
        else:
            print status

    def reply(self, mention):
        asker = mention['from_user']
        print asker + " said " + mention['text']
        status_id = str(mention['id'])
        if self.last_id_replied < status_id:
            self.last_id_replied = status_id
        self.tweet(status_id, asker)

    def replies(self):
        # get the status_id of the last tweet to which you replied
        replies = [tweet['in_reply_to_status_id']
                   for tweet in self.poster.statuses.user_timeline()
                   if tweet['in_reply_to_status_id'] is not None]
        try:
            self.last_id_replied = replies[0]
        except IndexError:
            self.last_id_replied = None
        results = []
        results = self.twitter.search(
            q="@"+self.handle,
            since_id=self.last_id_replied)['results']
        # do not reply to retweets
        retweets = re.compile('rt\s', flags=re.I)
        results = [response for response in results
                   if not retweets.search(response['text'])]
        if not results:
            print "Nobody's talking to me..."
        else:
            [self.reply(result) for result in results]
