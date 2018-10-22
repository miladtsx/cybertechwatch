#!/usr/bin/python2
import sys
sys.path.insert(0, './Helpers')
from Model import news, listOfnewsSources
import feedparser
from NewsHelper import DoesItMatch, freshNews

localNewsRepository = []
localRedundantNewsRepository = []


#redhat, oracle
# if description contains #important, then increase the priority

def UpdateNewsDB():
    for sourceUrl in listOfnewsSources:
        GetNewsOnline(sourceUrl)


def GetNewsOnline(url):
    try:
        RSSContent = feedparser.parse(url)
        #TODO Check For Null and Errors
        newsGot = RSSContent.entries
        if(len(newsGot) > 0):
            print '[' + str(RSSContent.status) + '] ' + url
        else:
            print '[' + str(RSSContent.status) + '] ' + url 

        for newsItem in newsGot:
            if(not freshNews(newsItem.published)):
                continue
            try:
                newsItemReceived = news(newsItem.title, newsItem.summary, newsItem.link, newsItem.published)
            except:
                newsItemReceived = news(newsItem.title, '', newsItem.link, newsItem.published)

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


if __name__ == "__main__":
    UpdateNewsDB()
    # newlist = sorted(localNewsRepository, key=lambda x: x.title, reverse=False)
    localNewsRepository.sort(key=lambda x: x.title)

    for i in localNewsRepository:
        print '- ' + i.title + '\n' + i.url + '\n'
    print 'Total News count: ' + \
        str(len(localNewsRepository)) + '\n' + '*' * 100

    for rn in localRedundantNewsRepository:
        print '\t[Redundant News] ' + rn.title + '\n' + rn.url

    else:
        pass
