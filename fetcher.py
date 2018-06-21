
#coding:utf-8
import urllib2
import time

def getData(url,header,data,method='get',isRetry=False,split=20,count=3):
    '''
    fetch all data from url
    '''
    print 'connecting......'
    isException = True
    c = 0
    while isException and c<=count:
        try:
            response = doRequest(url,header,data,method)
        except urllib2.URLError:
            if isRetry:
                c+=1
                print '连接超时或连接失败，即将重试......'+c
                time.sleep(split)
            else:
                print '连接超时或连接失败，退出......'
        else:
            isException = False
    return response.read()
    
    
def doRequest(url,header,data,method='get'):
    request = urllib2.Request(url,headers = header)
    if method=='post':request.add_data(data)
    response = urllib2.urlopen(request,timeout=30)  
    return  response
    
    
    
