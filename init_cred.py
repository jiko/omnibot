#!/usr/bin/env python

# Takes three arguments:
#   the name of your bot
#   your oauth access token
#   your oauth access token secret
# make sure your omni.cfg file points to the correct dot file

from twitter.oauth import write_token_file
import os
import sys
oauth_filename = os.environ.get('HOME', '') + os.sep + \
    '.' + sys.argv[1] + '_oauth'
write_token_file(oauth_filename, sys.argv[2], sys.argv[3])
