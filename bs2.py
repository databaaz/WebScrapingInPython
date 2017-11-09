import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL:')
html_data = urllib.urlopen(url).read()

mysoup = BeautifulSoup(html_data)

# mysoup = mysoup.prettify()
# print mysoup



a_tags = mysoup.find_all('a')  #or mysoup('a')

count = 1

for t in a_tags:
	print str(count) + '- TAG:',t
	print 'URL:',t.get('href',None)
	print 'Attributes:', t.attrs
	if len(t.contents)!=0:
		print 'Content:',t.contents[0]
	count = count + 1


