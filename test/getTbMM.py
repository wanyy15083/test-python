# -*- coding:utf-8 -*-

__author__ = 'SYG'

import urllib
import urllib2
import re
import os


class Tool:
    removeImg = re.compile('<img.*?>| {1,7}|&nbsp;')
    removeAddr = re.compile('<a.*?>|</a>')
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    replaceTD = re.compile('<td>')
    replacePara = re.compile('<p.*?>')
    replaceBR = re.compile('<br><br>|<br>')
    removeExtraTag = re.compile('<.*?>')
    removeNoneLine = re.compile('\n+')

    def replace(self, x):
        x = re.sub(self.removeImg, '', x)
        x = re.sub(self.removeAddr, '', x)
        x = re.sub(self.replaceLine, '\n', x)
        x = re.sub(self.replaceTD, '\t', x)
        x = re.sub(self.replacePara, '\n  ', x)
        x = re.sub(self.replaceBR, '\n', x)
        x = re.sub(self.removeExtraTag, '', x)
        x = re.sub(self.removeNoneLine, '\n', x)
        return x.strip()


class Spider:
    def __init__(self):
        self.siteURL = 'http://mm.taobao.com/json/request_top_list.htm'
        self.tool = Tool()

    def getPage(self, pageIndex):
        url = self.siteURL + '?page=' + str(pageIndex)
        print url
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getContents(self, pageIndex):
        page = self.getPage(pageIndex)
        pattern = re.compile(
            '<div class="list-item.*?pic-word.*?<a href="(.*?)".*?<img src="(.*?)".*?<a class="lady-name.*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>',
            re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            contents.append(['http:'+item[0], 'http:'+item[1], item[2], item[3], item[4]])
        return contents

    def getDetailPage(self, infoURL):
        response = urllib2.urlopen(infoURL)
        return response.read().decode('gbk')

    def getBrief(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        result = re.search(pattern, page)
        return self.tool.replace(result.group(1))

    def getAllImg(self, page):
        pattern = re.compile('<div class="mm-aixiu-content".*?>(.*?)<!--', re.S)
        content = re.search(pattern, page)
        patternImg = re.compile('<img.*?src="(.*?)"', re.S)
        images = re.findall(patternImg, content.group(1))
        return images

    def saveImgs(self,images,name):
        number = 1
        print u'发现',name,u'共有',len(images),u'张照片'
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if len(fTail) > 3:
                fTail = 'jpg'
            fileName = name + '/' + str(number) + '.' +fTail
            self.saveImg(imageURL,fileName)
            number +=1

    def saveIcon(self,iconURL,name):
        splitPath = iconURL.split('.')
        fTail = splitPath.pop()
        fileName = name + '/icon.' + fTail
        self.saveImg(iconURL,fileName)


    def saveImg(self, imageURL, fileName):
        u = urllib.urlopen(imageURL)
        data = u.read()
        f = open(fileName, 'wb')
        f.write(data)
        print u'正在报错她的图片：',fileName
        f.close()

    def saveBrief(self, content, name):
        fileName = name + '/' + name + '.txt'
        f = open(fileName, 'w+')
        print u'正在偷偷保存她的个人信息为', fileName
        f.write(content.encode('uft-8'))

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
            return True
        else:
            print u'文件夹',path,u'已创建成功'
            return False

    def savePageInfo(self,pageIndex):
        contents = self.getContents(pageIndex)
        for item in contents:
            print u'发现一位模特，名字叫',item[2],u'芳龄',item[3],u'她在',item[4]
            print u'正在保存',item[2],u'的信息'
            print u'又意外发现她的个人地址',item[0]
            detailURL = item[0]
            detailPage = self.getDetailPage(detailURL)
            brief = self.getBrief(detailPage)
            images = self.getAllImg(detailPage)
            self.mkdir(item[2])
            self.saveBrief(brief,item[2])
            self.saveIcon(item[1],item[2])
            self.saveImgs(images,item[2])
    def savePagesInfo(self,start,end):
        for i in range(start,end+1):
            print u'正在偷偷寻找第',i,u'个地方，看看MM们在不在'
            self.savePageInfo(i)

spider = Spider()
spider.savePagesInfo(2,10)
