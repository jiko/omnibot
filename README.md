=======
omnibot
=======

Python scripts and classes to make Twitter bot creation easier.

To manage a growing menagerie of bots, I consolidated my code into classes in a single location. Then I wrote a simple script to update every bot at once, hence the name. The bot runs via cron, like this:

	crontab -e
	0 */4 * * * python /home/jk/Code/bots/omnibot/omni.py

To use this code you will need to change the path in the cron definition, as well as in omni.py, to match the location of omnibot and your bot folders. Each bot folder contains:

	omni.cfg
	corpus.txt

Your corpus file can be named anything, as long as you specify it in omni.cfg. A sample configuration file (omni.cfg.sample) is included in this repository.

The init_cred.py script makes storing Twitter OAuth credentials easy. See the TODO.md file to see future plans, which include a detailed walkthrough of creating a configuration file.
