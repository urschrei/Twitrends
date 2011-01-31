#!/usr/bin/env python
# encoding: utf-8
"""
twitrend.py

Created by Stephan Hügel on 2011-01-31
"""

import sys
import os
import tweepy
import json


def open_file(to_read):
    """ Open a text file for reading, and strip the carriage returns
    """
    with open(to_read, 'r') as opened:
        # strip the newlines, and return the result as a list
        return [got_lines.rstrip() for got_lines in opened.readlines()]

def main():
    """ main function
    """
    oauth_values = open_file('acc_keys.txt')
    auth = tweepy.OAuthHandler(oauth_values[0], oauth_values[1])
    auth.set_access_token(oauth_values[2], oauth_values[3])
    api = tweepy.API(auth, secure = True)
    # now we can do whatever we like!
    woeid = 23424803
    loc_trends = api.trends_location(woeid)
    # dump the trends and associated metadata
    print json.dumps(loc_trends, sort_keys=True, indent=4)


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