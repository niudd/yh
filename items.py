#! /home/endi/anaconda/bin/python2.7


class YahooFinanceItem(object):
	def __init__(self, ID, Symbol, Name, Datetime, Price, Change, Change_Rate, Volume):
		self.ID = ID
		self.Symbol = Symbol
		self.Name = Name
		self.Datetime = Datetime
		self.Price = Price
		self.Change = Change
		self.Change_Rate = Change_Rate
		self.Volume = Volume

