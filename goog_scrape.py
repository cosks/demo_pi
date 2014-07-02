import urllib
import re

htmlfile = urllib.urlopen('https://www.google.co.uk/finance?q=AAPL')
htmltext = htmlfile.read()

regex = '<span id="ref_[^.]*_l">(.+?)</span>'

pattern = re.compile(regex)

results = re.findall(pattern,htmltext)

print results