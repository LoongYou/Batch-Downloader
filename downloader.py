#coding:utf-8
import urllib
import urllib2
import time
from net import fetcher
#--------------------------------config-------------------------------
#间隔多少秒下载，防止被发现
split = 3
#是否失败重试
isRetry=True
#重试间隔
retrysplit=10
#重试次数
retrycount=5
#文本资源后缀
suffix_doc = ('.txt','.html','.htm','.xml','.css','.js')
#二进制资源后缀
suffix_binary = ('.jpg','.jpeg','.png','.bmp','.gif')
#是否循环调用Referer，不少网站将当前页面url设置为referer
isReferer = True



values = {}
data = urllib.urlencode(values)
Referer = ''
User_Agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
#cookie = ''
upgrade_insecure_requests = 1
header = {
        'Referer':Referer,
        'User-Agent':User_Agent,
       # 'cookie':cookie,
       # 'upgrade-insecure-requests':upgrade_insecure_requests
    }


#--------------------------------program----------------------------------

def initRefere(re):
    if isReferer:
        header['Referer'] = re
        print  header['Referer']


def downloadOne(url,filePath,method='get'):
    '''
    download one object  one time but has less args
    一次连接下载一个文件
    '''
    if url and not None:
        index = int(url.rfind('.'))
        index2 = int(url.rfind(r'/'))
    else:
        print 'url is null'
        return False
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
