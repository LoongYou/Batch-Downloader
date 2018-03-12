
import urllib2

def fetchAll(url,header,data,method='get'):
    '''fetch all data from url'''
    print 'fetching......'
    request = urllib2.Request(url,headers = header)
    if method=='post':request.add_data(data)
    response = urllib2.urlopen(request,timeout=30)
    return response.read()
    
    
    