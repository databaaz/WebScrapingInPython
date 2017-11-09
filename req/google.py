from bs4 import BeautifulSoup
import sys
import requests
import webbrowser

if len(sys.argv)>1:
	query = ' '.join(sys.argv[1:])
else:
	print 'Please enter a query'
	quit()
try:
	result = requests.get('http://www.google.com/search?q='+query)
	result.raise_for_status()
except Exception as x:
	print 'Problem opening the page: %s' %x


mysoup = BeautifulSoup(result.text)
topres = mysoup.select('.r a')

count = min(5,len(topres))

for i in range(count):
	link = topres[i].get('href')
	webbrowser.open('http://google.com'+link)
