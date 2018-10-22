
class news():

    def __init__(self, title, description, url, date):
        self.title = title
        self.description = description
        self.url = url
        self.date = date
        self.priority = None

listOfnewsSources = [
    # 'https://exploit.kitploit.com/feeds/posts/default?alt=rss',
    # 'https://www.us-cert.gov/ncas/current-activity.xml',
    # 'https://www.us-cert.gov/ncas/alerts.xml',
    # 'https://ics-cert.us-cert.gov/alerts/alerts.xml',
    # 'https://ics-cert.us-cert.gov/advisories/advisories.xml',
    # 'https://www.secnews24.com/feed/',
    # 'https://securelist.com/feed/',
    # 'https://tools.cisco.com/security/center/psirtrss20/AlertRSS.xml',
    # 'https://tools.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml',
    # 'https://www.novell.com/newsfeeds/rss/patches/security_notifications-daily.xml',
    #'https://access.redhat.com/blogs/766093/feed',
    'https://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/rss-otn-sec.xml'
]

    #'https://www.certcc.ir/news/rss',