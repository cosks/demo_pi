import urllib
urls = ['http://google.com', 'http://mail.ru', 'http://yandex.ru']
i = 0

while i<len(urls):
	htmlfile = urllib.urlopen(urls[i])
	htmltext = htmlfile.read()
	print htmltext
	i+=1