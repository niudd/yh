#! /home/endi/anaconda/bin/python2.7


import requests
from pattern import web
import time, datetime
from items import YahooFinanceItem


def parse(response):
	'''
	The Format:
	ID 	           = 1
	Symbol         = u'ADM.L'
	Name           = u'Admiral Group plc'
	Datetime       = '2015-06-24 01:35:59'
	Price          = 1443.0
	Change         = -6.0
	Change_Rate(%) = 0.41
	Volume         = 322084

	'''

	Datetime = str(datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d %H:%M:%S'))
	html = response.text
	dom = web.Element(html)

	# ID points to which stock
	num=len(dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr'))
	print 'number of stocks: ', num
	for ID in range(1,num):

		print 'stock '+str(ID)
		try:
			Symbol = dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[0].by_tag('a')[0].content
			#print 'Symbol: ',Symbol

			Name = dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[1].content
			#print 'Name: ',Name

			Price = float(dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[2].by_tag('span')[0].content.replace(',',''))
			#print 'Price: ',Price

			_Sign = {'Up':'+', 'Down':'-'}
			_Change_directtion = _Sign[dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[3].by_tag('span')[0].by_tag('img')[0].attr['alt']]
			Change = float(_Change_directtion + dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[3].by_tag('span')[0].by_tag('b')[0].content)
			#print 'Change: ',Change

			Change_Rate = float(dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[3].by_tag('span')[1].by_tag('b')[0].content[2:-2])
			#print 'Change_Rate: ', Change_Rate

			Volume = int( dom.by_tag('table.yfnc_tableout1')[0].by_tag('table')[0].by_tag('tr')[ID].by_tag('td')[4].by_tag('span')[0].content.replace(',','') )
			#print 'Volume: ',Volume

			item = YahooFinanceItem(ID, Symbol, Name, Datetime, Price, Change, Change_Rate, Volume)
			yield item

		except:
			continue