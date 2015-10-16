#! /home/endi/anaconda/bin/python2.7


import spider
import settings
import requests
import random
import time
from request import *


urls_to_crawl = settings.start_urls
with open('request_headers/browser.txt', 'r') as f:
	browser_list = [item[:-1] for item in f.readlines()]
with open('request_headers/proxy_ip.txt', 'r') as f:
	ip_list = [item.split(',')[0] for item in f.readlines()]


def main():
	'''
	Test how many seconds does it take to request three pages by
	each proxy in the file "request_headers/browser.txt".
	Or whether it's a broken proxy that should be abandoned.

	'''


	for IP in ip_list:
		t0 = time.time()
		random_browser = random.choice(browser_list)
		headers = set_headers(random_browser)
		proxy_ip ={'http': IP}
		
		for url in urls_to_crawl:
			block = False
			try:
				response = requests.get(url, headers=headers, proxies=proxy_ip, timeout=5)
			except:
				print 'BLOCK: ',IP
				print '------------------------\n'*3
				block = True
				break

		if block:
			with open('request_headers/proxy_ip.txt', 'a') as f:
					f.write(IP+', BLOCK...\n')
		else:
			with open('request_headers/proxy_ip.txt', 'a') as f:
				f.write(IP+', consume time: %d seconds\n'%(time.time()-t0))
			print IP
			print 'consume time: %d seconds'%(time.time()-t0)
			print '\n'*2


if __name__ == "__main__":
	main()