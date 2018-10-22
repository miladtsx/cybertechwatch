import difflib
import sys
from datetime import datetime, timedelta
from dateutil import parser


def DoesItMatch(newItem, localRepoItem):
    if(difflib.SequenceMatcher(None, newItem, localRepoItem).ratio() > 0.9):
        #print '\t[Redundant News] ' + newItem + ' == ' + localRepoItem
        return True
    else:
        return False


def getYesterday():
    return str(datetime.now() - timedelta(days=1))[:10]


def freshNews(date):
    newsDate = str(parser.parse(date[:-3]))[:10]
    yesterday = getYesterday()
    return (newsDate >= yesterday)
