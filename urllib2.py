import urllib
import re

url = raw_input('Enter url: ')
site_data =  urllib.urlopen(url).read()    #read contents of the location

links = re.findall('href="(http://.+?)"',site_data)  #non-greedy matching of links

for x in links:
    print x
