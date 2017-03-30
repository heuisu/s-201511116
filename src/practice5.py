#coding: utf-8

import lxml.html
from lxml.cssselect import CSSSelector
import requests

rq = requests.get('http://www.ieee.org/conferences_events/conferences/search/index.html')
html = lxml.html.fromstring(rq.text)

select = CSSSelector('div.content-r-full table.nogrid-nopad tr p>a[href]')
nodes = select(html)
for node in nodes:
    print node.text
    print "----------"
