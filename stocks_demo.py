import urllib
import re

symbolslist = ['aapl','spy','goog','nflx']

i=0
while i<len(symbolslist):
	url = 'https://uk.finance.yahoo.com/q?s='+symbolslist[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()
	regex = '<span id="yfs_l84_'+symbolslist[i]+'">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	# price is an array, as it gathers all of the data where the condition is true, so we only want the 1st item
	print 'price of ',symbolslist[i],' is',price[0]
	i+=1