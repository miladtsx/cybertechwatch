import difflib
import sys
from datetime import datetime, timedelta
from dateutil import parser
from Model import listOfnewsSources, news, localNewsRepository, localRedundantNewsRepository
import feedparser




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


def UpdateNewsDB():
    for sourceUrl in listOfnewsSources:
        GetNewsOnline(sourceUrl)
    localNewsRepository.sort(key=lambda x: x.title)


def GetNewsOnline(url):
    try:
        RSSContent = feedparser.parse(url)
        # TODO Check For Null and Errors
        newsGot = RSSContent.entries
        if(len(newsGot) > 0):
            print '[' + str(RSSContent.status) + '] ' + url
        else:
            print '[' + str(RSSContent.status) + '] ' + url

        for newsItem in newsGot:
            if(not freshNews(newsItem.published)):
                continue
            try:
                newsItemReceived = news(
                    newsItem.title, newsItem.summary, newsItem.link, newsItem.published)
            except:
                newsItemReceived = news(
                    newsItem.title, '', newsItem.link, newsItem.published)

            if len(localNewsRepository) < 1:
                localNewsRepository.append(newsItemReceived)
                continue

            matchFound = False
            for localRep in localNewsRepository:
                if (DoesItMatch(newsItemReceived.title, localRep.title)):
                    matchFound = True
                    localRedundantNewsRepository.append(newsItemReceived)
                    break
                continue

            if(matchFound):
                continue
            else:
                localNewsRepository.append(newsItemReceived)
    except Exception, e:
        print '[Err] ' + url + '\n' + str(e)


def GetNewsOffline():
    NotImplementedError

def PrintNews():
    for i in localNewsRepository:
        print '- ' + i.title + '\n' + i.url + '\n'
    print 'Total News count: ' + \
        str(len(localNewsRepository)) + '\n' + '*' * 100

    for rn in localRedundantNewsRepository:
        print '\t[Redundant News] ' + rn.title + '\n' + rn.url