omnibot
=======

Python scripts and classes to simplify Twitter bot creation and management. Used to run [these bots](https://twitter.com/jmkp/lists/bots).

To create a new bot, run the `new-bot.py` script.

You can run the script at certain times via cron, like this:

	crontab -e
	0 */4 * * * python /path/to/omnibot/omni.py

Change the path in the cron definition to match the location of omnibot. You could also change omni.py to run as a daemon and have your bots tweet at different times.

The `bots.list` file stores a list of all your bot folders. 

Each bot folder contains:

	omni.cfg
	corpus.txt

Your corpus file can be named anything, as long as you specify it in omni.cfg or during the `new-bot.py` creation script. A sample configuration file `omni.cfg.sample` is included in this repository.

You can generate tweets with a 4-gram Markov model, the Isopsephy numerological model, or just grab a random line from the text. Look at the `bot.generate_text` method if you want to change/add text generation models.

todo
====
- Write a setup.py script that checks for deps and tries to install via pip
	- Depends on twitter, configparser
