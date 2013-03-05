=======
omnibot
=======

Python scripts and classes to make Twitter bot creation easier.

To manage a growing menagerie of bots, I consolidated my code, based on [shrinkbot](https://github.com/jiko/the_shrinkbot), into a class and put all bot-related classes in a single location. Then I wrote a simple script to update every bot at once, hence the name. The bot runs via cron, like this:

	crontab -e
	0 */4 * * * python /home/jk/Code/bots/omnibot/omni.py

To use this code you will need to change the path in the cron definition, as well as in omni.py, to match the location of omnibot and your bot folders, respectively. Store the list of bot folders in bots.list. Each bot folder contains:

	omni.cfg
	corpus.txt

Your corpus file can be named anything, as long as you specify it in omni.cfg. A sample configuration file (omni.cfg.sample) is included in this repository.

The init_cred.py script makes storing Twitter OAuth credentials easy. 

todo
====
- Expand on the init_cred.py script to automate the creation of a config file
	- Create a Twitter account for your bot
	- What is the Twitter username of your bot?
	- Create an app for this username at dev.twitter.com/apps/new
	- What is your Consumer Key?
	- What is your Consumer Secret?
	- What is your OAuth Access Token?
	- What is your OAuth Access Token Secret?
	- OK, now for the content of bot
	- What is the name of the corpus file for your bot? 
	- What method should we use to parse the corpus? (markov, isopsephy, random line)
- Write a setup.py script that checks for deps and tries to install via pip
	- Depends on twitter, configparser
