
class news():

    def __init__(self, title, description, url, date):
        self.title = title
        self.description = description
        self.url = url
        self.date = date
        self.priority = None

listOfnewsSources = [
    'http://securityaffairs.co/wordpress/feed ', 
    'https://access.redhat.com/blogs/766093/feed', 
    'https://cxsecurity.com/wlb/rss/all/', 
    'https://exploit.kitploit.com/feeds/posts/default?alt=rss', 
    'https://ics-cert.us-cert.gov/advisories/advisories.xml', 
    'https://ics-cert.us-cert.gov/alerts/alerts.xml', 
    'https://rss.packetstormsecurity.com/files/', 
    'https://searchsecurity.techtarget.com/rss/Security-Wire-Daily-News.xml', 
    'https://securelist.com/feed/', 
    'https://tools.cisco.com/security/center/psirtrss20/AlertRSS.xml', 
    'https://tools.cisco.com/security/center/psirtrss20/CiscoSecurityAdvisory.xml', 
    'https://twitrss.me/twitter_user_to_rss/?user=CVEnew', 
    'https://www.novell.com/newsfeeds/rss/patches/security_notifications-daily.xml', 
    'https://www.oracle.com/ocom/groups/public/@otn/documents/webcontent/rss-otn-sec.xml', 
    'https://www.secnews24.com/feed/', 
    'https://www.us-cert.gov/ncas/alerts.xml', 
    'https://www.us-cert.gov/ncas/current-activity.xml', 
    'https://www.vulnerability-lab.com/rss/rss.php',
    'https://securelist.com/feed/',
    'https://blog.yoroi.company/feed/',
    'http://feeds.feedburner.com/eset/blog/',
    'https://blog.malwarebytes.com/feed/',
    'https://www.certcc.ir/news/rss'
 ]

#Global variables
localNewsRepository = []
localRedundantNewsRepository = []
assetRelatedNewsItems = []
baselineDate = 1
assets=[ 'MariaDB', 'mysql', ' PHP ', ' ASP ', 'Ansible', 'Windows', 'ssh', 'Snmp', 'imaps',
        'pop3s', 'smtps']
