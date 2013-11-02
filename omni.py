#!/usr/bin/env python
from bot import Bot
import os


# keep a list of your bot folder names separated by newlines in the same folder as this script
bot_dir_list = os.path.dirname(__file__) + "bots.list"
bot_folders = []

with open(bot_dir_list) as f:
    bot_folders = f.read().splitlines()

# run all of your bots at once
for bot_folder in bot_folders:
    tweeter = Bot(bot_folder)
    tweeter.replies()
    tweeter.tweet()
