#-*- coding:utf-8 –*-
import urllib
import urllib2
import re
import thread
import time

class page3:
    def __init__(self):
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        self.url = 'http://www.zjjrc.com/job/list/0-0-0-0_0_0_0_0_0-0-0-0-3.html'
        self.headers = {'User-Agent':self.user_agent}

    def getpage(self, index):
        user_agent=self.user_agent
        url=self.url
        headers=self.headers
        result = urllib2.Request( url, headers=headers )
        response = urllib2.urlopen(result)
        pageCode = response.read()
        pattern = re.compile(r'<a href=.*?class="search_job_jobs_name yun_text_color".*?>(.*?)</a>.*?<span class="job_search_xz">(.*?)</span>.*?<em class="com_search_job_em">(.*?)</em>.*?<em class="com_search_job_em">(.*?)</em>.*?<em class="com_search_job_em">(.*?)</em>',re.S)
        items = re.findall(pattern, pageCode)
        for i in items:
            input = raw_input()
            for g in i:
                print g



    def start(self):
        print "--------------------------------------page3------------------------------------"
        print "-------------             i'm    Separation   line         --------------------"
        self.getpage(index=page3)
        
