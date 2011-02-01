#!/usr/bin/env python
# encoding: utf-8
"""
twitrend.py

Requires OAuth values in a text file, in the following order:

Consumer key
Consumer secret
Access key
Access secret

Specify filename on line 36
"""


import sys
import tweepy


def open_file(to_read):
    """ Open a text file for reading, and strip the carriage returns
    """
    try:
        with open(to_read, 'r') as opened:
            # strip the newlines, and return the result as a list
            return [got_lines.rstrip('\n') for got_lines in opened.readlines()]
    except IOError:
        print "Couldn't read OAuth values from %s\nCan't continue." % to_read
        raise


def main():
    """ main function
    """
    oauth_values = open_file('/Users/sth/dev/twitrend/acc_keys.txt')
    auth = tweepy.OAuthHandler(oauth_values[0], oauth_values[1])
    auth.set_access_token(oauth_values[2], oauth_values[3])
    try:
        api = tweepy.API(auth, secure = True)
        # now we can do whatever we like!
        # Ireland's WOEID. Get your own here:
        woeid = 23424803
        retrieved = api.trends_location(woeid)
    except tweepy.TweepError:
        print "Couldn't retrieve trends. Error was:"
        raise
    # the following is required because the trends_location method returns a
    # single-member list containing a JSON-formatted dict, *not* a JSON object
    names = [trend["name"] for trend in retrieved[0]["trends"]]
    print '\n'.join(names)


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        # actually raise these, for a clean exit
        raise
    except Exception, error:
        # all other exceptions: display the error
        print error
    else:
        pass
    finally:
        # exit cleanly once we've done everything else
        sys.exit(0)