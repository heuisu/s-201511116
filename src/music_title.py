import lxml.html
from lxml.cssselect import CSSSelector
import urllib
#coding: utf-8

keyword='rain'
f=urllib.urlopen("http://music.naver.com/search/search.nhn?query="+keyword+"&x=0&y=0")
mydata =f.read()

html = lxml.html.fromstring(mydata)
#tree=lxml.etree.parse('myhtml')
# construct a CSS Selector -> 
sel = CSSSelector('#content > div:nth-child(4) \
    > div._tracklist_mytrack.tracklist_table.tracklist_type1._searchTrack \
    > table > tbody > tr > td.name > a.title')
# Apply the selector to the DOM tree.
nodes = sel(html)

for node in nodes:
    #print lxml.html.tostring(item)
    print node.text_content()