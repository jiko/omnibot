#!/usr/bin/env python

import os

print "Create a new Twitter account: https://twitter.com/signup"
print "What is the Twitter username for your bot?"
BOT_NAME = raw_input()
FULL_PATH = os.path.dirname(__file__) + os.sep + BOT_NAME
os.mkdir(FULL_PATH)
CFG_FILE = FULL_PATH + "/omni.cfg"
CFG = "[" + BOT_NAME + "]\n"
CFG += "handle=" + BOT_NAME + "\n"
print "Create an app for this username at https://dev.twitter.com/apps/new"
OAUTH_FILE = os.path.dirname(__file__) + os.sep  + BOT_NAME + "_oauth"
CFG += "oauth=" + OAUTH_FILE + "\n"
print "What is your Consumer Key?"
CONSUMER_KEY = raw_input()
CFG += "consumer_key=" + CONSUMER_KEY + "\n"
print "What is your Consumer Secret?"
CONSUMER_SECRET = raw_input()
CFG += "consumer_secret=" + CONSUMER_SECRET + "\n"
print "What is your OAuth Access Token?"
ACCESS_TOKEN = raw_input()
print "What is your OAuth Access Token Secret?"
ACCESS_SECRET = raw_input()
with open(OAUTH_FILE, 'w') as o:
    o.write(ACCESS_TOKEN + "\n")
    o.write(ACCESS_SECRET + "\n")
print "OK, now for the content of bot"
print "What is the name of the corpus file for your bot?"
FILE_NAME = raw_input()
CFG += "corpus=" + FILE_NAME + "\n"
print "What method should we use to generate text from the corpus?"
print "Choose between markov, isopsephy, or random"
METHOD = raw_input()
CFG += "tweet_method=" + METHOD + "\n"
with open(CFG_FILE, 'w') as cfg:
    cfg.write(CFG)
print "Done!"
