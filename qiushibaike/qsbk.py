# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
	request = urllib2.Request(url, headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	pattern = re.compile('<h2>(.*?)</h2>.*?<span>(.*?)</span>.*?<a.*?>.*?<img src=(.*?).*?>.*?</a>.*?<i class="number">(.*?)</i>',re.S)

	items = re.findall(pattern,content)
	for item in items:
		print item[3]
	
except urllib2.URLError, e:
	if hasattr(e, "code"):
		print e.code
	if hasattr(e, "reason"):
		print e.reason

