#!/usr/bin/env python
from bot import Bot
import os
# change this to the folder where your bots live
bots_root = "/home/jk/Code/bots/"
# keep a list of your bots folder names separated by newlines,
# in the same folder as this script
bot_dir_list = os.path.dirname(__file__) + "/bots.list"
bot_folders = []
with open(bot_dir_list) as f:
    bot_folders = f.read().splitlines()
for bot_folder in bot_folders:
    tweeter = Bot(bot_folder, bots_root)
#    tweeter.replies()
    tweeter.tweet()
