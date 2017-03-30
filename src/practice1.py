
import urllib

response = urllib.urlopen('http://python.org/')
_html = response.read()
print len(_html)
print type(_html)
print response.info()
