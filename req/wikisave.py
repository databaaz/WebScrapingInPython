from bs4 import BeautifulSoup
import sys
import requests
import webbrowser

if len(sys.argv)>1:
	query = '_'.join(sys.argv[1:])
else:
	print 'Please enter a query'
	quit()
try:
	result = requests.get('https://en.wikipedia.org/wiki/'+query)
	result.raise_for_status()
except Exception as x:
	print 'Problem opening the page: %s' %x


mysoup = BeautifulSoup(result.text)

div = mysoup.select('#mw-content-text')[0]
children = div.findChildren()
p=[]
for child in children:
	if (child.name=='p' or child.name=='h1' or child.name=='h2' or child.name=='h3' or child.name=='h4') and child.parent.name!='td':
		p.append(child)

filename= query+'.txt'
handle1 = open(filename,'wb')	
for i in p:
	text = '\n\n' + i.text.encode('utf-8')
	handle1.write(text)


