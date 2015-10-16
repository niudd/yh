#! /home/endi/anaconda/bin/python2.7


import requests
from pattern import web


def main():
	urls = ['http://www.useragentstring.com/pages/Chrome/',\
		   'http://www.useragentstring.com/pages/Firefox/',\
		   'http://www.useragentstring.com/pages/Mozilla/']
	for url in urls:
		print 'parsing: ',url
		html = requests.get(url).text
		dom = web.Element(html)
		browsers = [dom.by_tag('ul')[index].by_tag('a')[0].content for index in range(len(dom.by_tag('ul')))]
		with open('browser.txt', 'a') as f:
			for browser in browsers:
				f.write(browser+'\n')
		print 'finish: '+url+'\n'



if __name__ == "__main__":
	main()