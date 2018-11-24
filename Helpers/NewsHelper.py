from Model import listOfnewsSources, news, localNewsRepository, localRedundantNewsRepository, assetRelatedNewsItems, assets
from HelperMethods import doesItMatch, getRSSContent, freshNews
from TaskHelper import taskRun
import traceback

def updateNewsDB():

    taskRun(getNewsOnline, listOfnewsSources, len(listOfnewsSources))
    
    for redunItem in localRedundantNewsRepository:
        print '[Match] ' + redunItem.title[:100]
    
    if (len(assetRelatedNewsItems) > 0):
            print '*' * 10 + 'ASSETS' + '*' * 10 
            for assetItem in assetRelatedNewsItems:
                print '[ ' + assetItem.title[:100] + ' ]'

def getNewsOnline(url):
    try:
        webContent = getRSSContent(url)
        
        if(len(webContent) < 1):
            return

        
        newsGot = webContent.entries
        if(len(newsGot) > 0):
            print '\r' + '[' + str(webContent.status) + '] ' + url
        else:
            print '\r' + '[Err] ' + url
            return
        if (webContent.status != 200):
            return

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

            try:

                for asset in assets:
                    if(asset.lower() in newsItem.title.lower()):
                        assetRelatedNewsItems.append(newsItem)
            except:
                raise TypeError("Checking the Assets Failed!")

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
    except Exception:
        print '[Err] ' + url + '\n' + traceback.print_exc()
