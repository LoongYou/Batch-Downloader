
import urllib
import urllib2
import time
from net import fetcher

suffix_doc = ('.txt','.html','.htm','.xml','.css','.js')
suffix_binary = ('.jpg','.jpeg','.png','.bmp','.gif')


values = {}
data = urllib.urlencode(values)
Referer = ''
User_Agent = ''

header = {
        'Referer':Referer,
        'User-Agent':User_Agent
    }


def downloadOne(url,filePath,split = 1,method='get'):
    '''
    download one object  one time but has less args
    '''
    index = int(url.rfind('.'))
    index2 = int(url.rfind(r'/'))
    if index==-1:print 'unknow suffix'
    fileSuffix = url[index:len(url)]
    fileName = url[index2:index]
    print 'downloading:'+url
    try:
        
        saveFile(filePath+fileName+fileSuffix,
                 fetcher.fetchAll(url,header,data,method),
                 modeSelect(fileSuffix))
        time.sleep(split)
        
    except urllib2.HTTPError,e:
        if hasattr(e, 'code') and hasattr(e, 'reason'):
            print e.code,' '+e.reason

def saveFile(fileName,data,mode = 'wb+'):
    '''write file'''
    fileobj = open(fileName,mode)
    fileobj.write(data)
    fileobj.close()
    
def modeSelect(Suffix):
    '''according the suffix return the writing-mode'''
    mode = 'w'
    if (Suffix in suffix_binary):
        mode = 'wb+'
    return mode
    
def downloadDate(url,method='get'):
    '''just get data from url'''
    return fetcher.fetchAll(url, header, data, method)