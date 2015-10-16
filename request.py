#! /home/endi/anaconda/bin/python2.7


import spider
import pipelines
import settings
import requests
import random
#import pandas as pd


def set_headers(browser=None):
	'''
	Set requests headers.

	Parameters:

	browser: str, 'User-Agent'; None, default browser

	'''
	if browser:
		return {\
			'User-Agent':browser, \
			'Referer':'http://finance.yahoo.com/', \
			'Host':'finance.yahoo.com', \
			#'Cookie':'B=4jntf1hacmof8&b=3&s=t8; ywandp=1000911397279%3A3233539774; fpc=1000911397279%3AZT0hvRo1%7C%7C; ywadp115488662=738638268; ypcdb=acf23f08c7de1c954f17447ea3272d81; yvapF=%7B%22vl%22%3A1%2C%22rvl%22%3A1%7D; PRF=&t=^FTSE+JMAT.L+ABF.L+AAL.L+BNZL.L+LSE.L+RBS.L+AAPL+^SPSUPX+YHOO+^GSPC', \
			'Connection':'keep-alive', \
			'Cache-Control':'max-age=0', \
			'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,fr;q=0.2', \
			'Accept-Encoding':'gzip, deflate, sdch', \
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
			}
	else:
		return {\
			'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/41.0.2272.76 Chrome/41.0.2272.76 Safari/537.36', \
			'Referer':'http://finance.yahoo.com/', \
			'Host':'finance.yahoo.com', \
			#'Cookie':'B=4jntf1hacmof8&b=3&s=t8; ywandp=1000911397279%3A3233539774; fpc=1000911397279%3AZT0hvRo1%7C%7C; ywadp115488662=738638268; ypcdb=acf23f08c7de1c954f17447ea3272d81; yvapF=%7B%22vl%22%3A1%2C%22rvl%22%3A1%7D; PRF=&t=^FTSE+JMAT.L+ABF.L+AAL.L+BNZL.L+LSE.L+RBS.L+AAPL+^SPSUPX+YHOO+^GSPC', \
			'Connection':'keep-alive', \
			'Cache-Control':'max-age=0', \
			'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,fr;q=0.2', \
			'Accept-Encoding':'gzip, deflate, sdch', \
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8' \
			}


def make_request(url, ip_list, browser_list, proxy=False):
	'''
	Randomly choose a ip_proxy and brower to make a request.
	Return a response if succeed, return 'None' if fail.

	Parameters:
	url: str, request url
	ip_list: list, ip proxies to choose
	browser_list: list, browsers to choose
	proxy: True or False, whether use proxy or not.

	'''


	if proxy:
		random_browser = random.choice(browser_list)
		headers = set_headers(random_browser)
		random_ip = random.choice(ip_list)
		proxy_ip ={'http':random_ip}
		try:
			response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=2)
			if len(response.text) < 40000:
				return None
			else:
				return response
		except:
			return None

	else:
		try:
			headers = set_headers()
			response = requests.get(url, headers=headers, timeout=2)
			if len(response.text) < 40000:
				return None
			else:
				return response
		except:
			return None