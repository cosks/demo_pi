import urllib
import re

#htmlfile = urllib.urlopen('https://www.google.co.uk/finance?q=AAPL')

# making a strait forward request to the server without the webpage
htmlfile = urllib.urlopen('https://www.google.co.uk/finance/getprices?q=AAPL&x=NASD&i=120&p=25m&f=c&df=cpct&auto=1&ts=1404326982484&ei=CVS0U_DUHc-uwAPt9YCYCg')
htmltext = htmlfile.read()

regex = '<span id="ref_[^.]*_l">(.+?)</span>'

pattern = re.compile(regex)

results = re.findall(pattern,htmltext)

#print results

print htmltext.split()[len(htmltext.split())-1]