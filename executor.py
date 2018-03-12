#!/user/bin/env python
#coding:utf-8
from bs4 import BeautifulSoup
from net import downloader
import os

downloader.User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

#your hostname
host = ''
#special first page(if has),not include hostname
firstPage = ''
#the same of every url,not include hostname
generalPage = ''
#the page type
pageSuffix = '.html'
#the local path that to the download file
saveDir = 'D:\\images\\'
#the tag to mathch
attrs = {'class':''}

def getPage(hasFirst = 0):
    '''Dose the url of first page need to special deal?'''
    if hasFirst == 1:
        return host+firstPage
    else:
        return host+generalPage
    
def addzero(add,var=1,offset=10):
    '''Do you want to add 0 when the number<10?'''
    if add:
        if var<offset:
            return '0'+str(var)
        else:
            return str(var)
    else:
        return str(var)
    
def downloadIter(start = 1,offset = 1,add = False,firstSet = False,eachDir = False):
    '''connect and fetching and download iterative
    add = if add 0,firstSet = if special deal with first page url,eachDir = if every url file save in the same dir'''
    i = start
    for index in range(start,offset+1):
        index = addzero(add,index,offset+1)
        if firstSet:
            if i==1:
                url = getPage(1)+pageSuffix
            else:
                url = getPage(0)+index+pageSuffix
        else:
            url = getPage()+index+pageSuffix
        print '>>>>>>>>>>>>>>>>>>>>>>>>downloadPage:'+url
        downloader.Referer = 'url'
        html = downloader.downloadDate(url)
        bs = BeautifulSoup(html,'lxml')
        if eachDir:
            savePath = saveDir+bs.title.string+'['+index+']'
            if not os.path.exists(savePath):    
                os.mkdir(savePath)
        elif i!=0:
            savePath = saveDir+bs.title.string
            if not os.path.exists(savePath):    
                os.mkdir(savePath)
        for url in downloadFind(bs,'img',attrs):
            link = url.get('src')
            downloader.downloadOne(link,savePath)
        i = 0
    print '===================finish==================='
      
def downloadFind(bs,name=None, attrs={}, recursive=True, text=None, limit=None):
    '''matching pattern and return the list of result'''
    res = bs.find_all(name, attrs, recursive, text, limit)
    print 'search result:'
    for item in res:
        print item
    print '============================================'
    return res


#start your
downloadIter(1,4,firstSet = True)

