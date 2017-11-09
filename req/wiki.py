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
	quit()


mysoup = BeautifulSoup(result.text)

div = mysoup.select('#mw-content-text')[0]   
children =  div.find_all('p')#div.findChildren()
p=[]
for child in children:
	if child.name=='p' and child.parent.name!='td':
		p.append(child)
	if   child.text=='':#len(child.contents)==0:                   #'class' in child.attrs and child['class'] == ['toc']:
		break	
	
if len(p)!=0:
	for i in p:
		print '\n'+i.text
else:
	print 'Please be more clear in your search'
