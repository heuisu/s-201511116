#!/usr/bin/env python
# coding: utf-8
import os
import requests
import urlparse
import urllib
import mylib

def doIt():
    # (1) service + operation
    SERVICE='ArpltnInforInqireSvc'
    OPERATION_NAME='getMinuDustFrcstDspth'
    #params1=os.path.join(SERVICE,OPERATION_NAME)
    params1 = SERVICE+"/"+OPERATION_NAME
    # (2) query params encoding
    _d=dict()
    _d['dataTerm']='month'
    params2 = urllib.urlencode(_d)
    # (3) add my service key
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    keygokr=key['gokr '] # keygokr='8Bx4C1%2B...'
    params=params1+'?'+'serviceKey='+keygokr+'&'+params2
    # (4) make a full url
    _url='http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc'
    url=urlparse.urljoin(_url,params)
    # (5) get data
    data=requests.get(url).text
    print data[:300]

if __name__ == "__main__":
    doIt()