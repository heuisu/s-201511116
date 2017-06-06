
from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://openapi.jbfood.go.kr:8080/openapi/service/FoodDictionaryService/getFoodDictionary'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'hdlADiXYqJN1a6zbqY4HMvgzSyaT23LyV4%2F%2Ftx63D%2BltBqj0wFFGsbS%2B97kFN8C80VzYfRM%2BlfSMd5dbXGmgPQ%3D%3D ', quote_plus('Category') : 'A' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print response_body