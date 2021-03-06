# Description #

A python script to output the top ten Twitter trending topics (based on [WOEID][1]) to [Growlnotify][2]

# Setup #

Put `twitrend.py` and `acc_keys.txt` in your path, ensure the script is executable, and call it from e.g. a shell script, or cron:  
`twitrend.py | growlnotify -a Twitter -t Twitter Trends`  

If calling from cron, bear in mind that the script runs in your home directory, and will look for `acc_keys.txt` there. Its log file will also be written there.

The `-a` switch assumes you have the [Twitter][3] app installed.  

Requires the [Tweepy][4] library, and OAuth credentials for your Twitter account.  
If you don't know how to obtain these, download and run the script found [here][5].  
`acc_keys.txt` should have the following format:  

`consumer key`  
`consumer secret`  
`access key`  
`access secret`  

[1]:    http://en.wikipedia.org/wiki/WOEID
[2]:    http://growl.info/extras.php
[3]:    http://itunes.apple.com/app/twitter/id409789998?mt=12
[4]:    https://github.com/joshthecoder/tweepy
[5]:    https://github.com/urschrei/Plowman/blob/master/getOAuth.py