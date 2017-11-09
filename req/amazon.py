#! /usr/bin/python


#search amazon with given query & open top 5 results


from bs4 import BeautifulSoup
import sys
import requests
import webbrowser

if len(sys.argv)>1:
	query = ' '.join(sys.argv[1:])
else:
	print 'Please enter a query'
	quit()

#url= 'https://www.snapdeal.com/search?keyword='+ query+'&sort=plth'

url = 'https://www.amazon.in/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+query

try:
	result = requests.get(url)
	result.raise_for_status()
except Exception as x:
	print 'Problem opening the page: %s' %x


print result.url

mysoup = BeautifulSoup(result.text)
topres = mysoup.select('a > h2')

count = min(5,len(topres))

for i in range(count):
	link = topres[i].parent.get('href')
	webbrowser.open(link)


