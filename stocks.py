import urllib
import re

symbolfile = open("symbols.txt")

symbolslist = symbolfile.read()

print symbolslist.split("\n")


#symbolslist = ['aapl','spy','goog','nflx']

symbolslist = symbolslist.split("\n")

#later to change so that it ignores the upercase and makes all lower case
#symbolslist=("${symbolslist[@],,}")

# this is a LINIER IMPLEMINTATION as the requests go in one at a time


i=0
while i<len(symbolslist):
	url = 'https://uk.finance.yahoo.com/q?s='+symbolslist[i]
	htmlfile = urllib.urlopen(url)
	htmltext = htmlfile.read()

	# old: regex = '<span id="yfs_l84_'+symbolslist[i]+'">(.+?)</span>'
	regex = '<span id="yfs_l84_[^.]*">(.+?)</span>'
	pattern = re.compile(regex)
	price = re.findall(pattern,htmltext)
	# price is an array, as it gathers all of the data where the condition is true, so we only want the 1st item
	print 'price of ',symbolslist[i],' is',price[0]
	i+=1