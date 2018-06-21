#coding:utf-8
import urllib
import urllib2
import time
from net import fetcher
#--------------------------------config-------------------------------
#是否失败重试
isRetry=True
#重试间隔
retrysplit=30
#重试次数
retrycount=5
#文本资源后缀
suffix_doc = ('.txt','.html','.htm','.xml','.css','.js')
#二进制资源后缀
suffix_binary = ('.jpg','.jpeg','.png','.bmp','.gif')




values = {}
data = urllib.urlencode(values)
Referer = ''
User_Agent = ''

header = {
        'Referer':Referer,
        'User-Agent':User_Agent
    }


#--------------------------------program----------------------------------

def downloadOne(url,filePath,split = 5,method='get'):
    '''
    download one object  one time but has less args
    一次连接下载一个文件，split=间隔多少秒，防止被发现
    '''
    index = int(url.rfind('.'))
    index2 = int(url.rfind(r'/'))
    if index==-1:print 'unknow suffix'
    fileSuffix = url[index:len(url)]
    fileName = url[index2:index]
    print 'downloading:'+url
    try:
        
        saveFile(filePath+fileName+fileSuffix,
                 fetcher.getData(url,header,data,method,isRetry,retrysplit,retrycount),
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
    '''
    according the suffix return the writing-mode
   根据文件后缀决定使用字符还是二进制格式保存文件
    '''
    mode = 'w'
    if (Suffix in suffix_binary):
        mode = 'wb+'
    return mode
    
def downloadDate(url,method='get'):
    '''just get data from url'''
    return fetcher.getData(url, header, data, method,isRetry,retrysplit,retrycount)
