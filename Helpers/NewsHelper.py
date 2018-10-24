from Model import listOfnewsSources, news, localNewsRepository, localRedundantNewsRepository
from HelperMethods import doesItMatch, getRSSContent, freshNews
from TaskHelper import taskRun

def updateNewsDB():

    taskRun(getNewsOnline, listOfnewsSources, len(listOfnewsSources))

def getNewsOnline(url):
    try:
        webContent = getRSSContent(url)
        # TODO Check For Null and Errors

        newsGot = webContent.entries
        if(len(newsGot) > 0):
            print '\r' + '[' + str(webContent.status) + '] ' + url
        else:
            print '\r' + '[' + str(webContent.status) + '] ' + url

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
                if (doesItMatch(newsItemReceived.title, localRep.title)):
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