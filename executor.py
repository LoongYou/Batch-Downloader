#!/user/bin/env python
#coding:utf-8
from bs4 import BeautifulSoup
from net import downloader
import os


#--------------------------------config-------------------------------

#your hostname 你想爬取的连接主机名，可以理解为不变的部分,如：
host = 'http://aaa.net/bbbl/2017/photo/'
#special first page(if has),not include hostname 第一页不一样的部分
firstPage = '2850'
#the same of every url,not include hostname 此后每一页都一样的部分
generalPage = '2850_'
#the page type 页面后缀
pageSuffix = '.html'
#the local path that to the download file 文件保存路径
saveDir = 'D:\\image\\' 
#目标元素类型
targetType = 'img'
#the tag to mathch 用于匹配的目标元素的属性
attrs = {'alt':'[photo]beauty'}
#要获取匹配元素的目标属性
targetAtt = 'src'
#起始页
start = 1
#结束页
offset = 11


#--------------------------------program----------------------------------

downloader.User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

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
    
def downloadIter(noFirst = False,start = 1,offset = 1,add = False,firstSet = False,eachDir = False):
    '''connect and fetching and download iterative
    add = if add 0,firstSet = if special deal with first page url,eachDir = if every url file save in the same dir'''
    '''递归的连接并爬取和下载
    noFirst:第一页是否包含页数，不少网站帖子的第一页是没有页数的
    start：起始页数
    offset：结束页数
    add：页数小于10是否前面加0
    firstSet：第一页url是否跟后面页数不一样，如果不一样则使用firstPage给定的url
    eachDir：是否将所有页面文件都保存在同一个目录里
    '''
    i = start
    for index in range(start,offset+1):
        index = addzero(add,index,offset+1)
        if firstSet:
            if i==1:
                url = getPage(1)+pageSuffix
            else:
                url = getPage(0)+index+pageSuffix
        else:
            if noFirst:
                url = getPage()+pageSuffix
            else:
                url = getPage()+index+pageSuffix
        print '>>>>>>>>>>>>>downloadPage:'+url
        downloader.Referer = 'url'
        html = downloader.downloadDate(url)
        bs = BeautifulSoup(html,'lxml')
        if eachDir:
            pindex = index
            pindex = str(pindex)
            savePath = saveDir+bs.title.string+'['+pindex+']'
            if not os.path.exists(savePath):    
                os.mkdir(savePath)
        elif i!=0:
            savePath = saveDir+bs.title.string
            if not os.path.exists(savePath):    
                os.mkdir(savePath)
        for url in downloadFind(bs,targetType,attrs):
            link = url.get(targetAtt)
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

#start your batch download
downloadIter(True,start,offset,firstSet = True)

