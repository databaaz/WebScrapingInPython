import urllib
from bs4 import BeautifulSoup

html_data = urllib.urlopen('http://www.vcet.edu.in').read()

mysoup = BeautifulSoup(html_data)



a_tags = mysoup('a')  #or mysoup.find_all('a')



for t in a_tags:
    print t.get('href')


"""
find_all(self, name=None, attrs={}, recursive=True, text=None, limit=None, **kwargs) unbound bs4.BeautifulSoup method
    Extracts a list of Tag objects that match the given
    criteria.  You can specify the name of the Tag and any
    attributes you want the Tag to have.
    
    The value of a key-value pair in the 'attrs' map can be a
    string, a list of strings, a regular expression object, or a
    callable that takes a string and returns whether or not the
    string matches for some custom definition of 'matches'. The
    same is true of the tag name.




t = mysoup.find_all({'a':'href'})
print t
for i in t:
	print i
"""
