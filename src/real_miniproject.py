#encoding: utf-8
import os
import requests
import urlparse
import mylib
import json


def doIt():
    keyPath=os.path.join(os.getcwd(), 'src', 'key.properties')
    key=mylib.getKey(keyPath)
    KEY=key['opendata']
    TYPE='json'
    SERVICE='ForecastWarningOzoneService'
    START_INDEX=int(1)
    END_INDEX=int(10)
    params='/'+KEY+'/'+TYPE+'/'+SERVICE+'/'+str(START_INDEX)+'/'+str(END_INDEX)
    _url='http://openAPI.seoul.go.kr:8088/555a55797068656533364a45715a41/xml/ForecastWarningOzoneService/1/5/'
    url=urlparse.urljoin(_url,params)
    data=requests.get(url).text
    
    jd=json.loads(data)
    for item in jd['ForecastWarningOzoneService']['row']:
        #print item.keys()
        for i in item.keys():
            if i=='ALARM_CNDT':
                #print ''.join(item.values())
                print item.values()[5]

if __name__ == "__main__":
    doIt()