#! /home/endi/anaconda/bin/python2.7


import spider
import pipelines
import settings
import requests
import random
from request import *
#import pandas as pd

'''
avoid getting banned:
http://doc.scrapy.org/en/latest/topics/practices.html#bans

random User-Agent:
http://www.useragentstring.com/pages/useragentstring.php

random proxy_ip:
http://www.ip-adress.com/proxy_list/?k=time&d=desc

'''


# a list of three YahooFinance urls to parse.
urls_to_crawl = settings.start_urls
# a list of browser to choose.
with open('request_headers/browser.txt', 'r') as f:
	browser_list = [item[:-1] for item in f.readlines()]
# a list of ip proxies to choose.
with open('request_headers/proxy_ip.txt', 'r') as f:
	ip_list = [item.split(',')[0] for item in f.readlines()]
# a dataframe to rank the IPs by speed of making requests
#ip_df = pd.DataFrame({'IP': ip_list, 'speed':[0]*len(ip_list)})


def run():
	while True:

		for url in urls_to_crawl:
			print url

			proxy = False

			print '1 requests...'
			response = make_request(url, ip_list, browser_list, proxy)
			if not response:
				print 'fail...\n--------------------------------------'
				proxy = True

			t = 2
			while not response:
				print '%d requests...' %t
				t += 1
				response = make_request(url, ip_list, browser_list, proxy)
			print 'requests succeed...\n--------------------------------------'


			print 'parsing page...'
			item = spider.parse(response)

			print 'collecting into database...'
			pipelines.process_item(item)

			print 'finish this page\n--------------------------------------'


if __name__ == '__main__':
	run()