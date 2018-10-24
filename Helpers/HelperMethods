from datetime import datetime, timedelta
from dateutil import parser
from Model import baselineDate
import difflib
import feedparser


# determine the baseline date where News before that day, should be ignored.
# 1 --> just news which was published 24 hours ago
# 3 --> News which published 3 days ago
def getBaselineDate():
    return str(datetime.now() - timedelta(days=baselineDate))[:10]

def freshNews(date):
    newsDate = str(parser.parse(date[:-3]))[:10]
    return newsDate >= getBaselineDate()

def printNews(newsItems):
    for i in newsItems:
        print '- ' + i.title + '\n' + i.url + '\n'
    print 'Total News count: ' + \
        str(len(newsItems)) + '\n' + '*' * 100

# Compare two string
def doesItMatch(str1, str2):
    if(difflib.SequenceMatcher(None, str1, str2).ratio() > 0.9):
        return True
    else:
        return False

def getFileName():
    return './reports/' + datetime.today().strftime("%B-%d-%Y.docx")

def getRSSContent(url):
    return feedparser.parse(url)