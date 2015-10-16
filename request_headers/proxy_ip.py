#! /home/endi/anaconda/bin/python2.7


'''
There are 3 levels of proxies according to their anonymity.

Level 1 - Elite Proxy / Highly Anonymous Proxy: The web server can't detect whether you are using a proxy.
Level 2 - Anonymous Proxy: The web server can know you are using a proxy, but it can't know your real IP.
Level 3 - Transparent Proxy: The web server can know you are using a proxy and it can also know your real IP.
'''

import requests
from pattern import web


def main():
	url = 'http://www.ip-adress.com/proxy_list/?k=time&d=desc'
	html = requests.get(url).text
	dom = web.Element(html)

	ip_item = dom.by_tag('tr.odd')+dom.by_tag('tr.even')

	for index in range(50):
		IP = ip_item[index].by_tag('td')[0].content
		IP_Type = ip_item[index].by_tag('td')[1].content
		if IP_Type == 'Elite':
			with open('proxy_ip.txt', 'r') as f:
				collected_ip = [ip[7:-1] for ip in f.readlines()]
			with open('proxy_ip.txt', 'a') as f:
				if IP not in collected_ip:
					f.write('http://'+IP+'\n')


if __name__ == "__main__":
	main()