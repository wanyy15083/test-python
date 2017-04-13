# -*- coding: utf-8 -*-

import os

rootPath = 'D:\\Java\\Git\\'


def eachPath(filePath):
    childs = []
    paths = os.listdir(filePath)
    for path in paths:
        childPath = os.path.join("%s%s" % (filePath, path))
        childs.append(childPath)
        # print "cmd.exe /k cd " + childPath.decode("gbk") + " && git pull"
        # os.system("cmd.exe /k cd " + childPath.decode("gbk") + " && git pull")
    return childs


def checkGit(paths):
    for path in paths:
        files = os.listdir(path)
        if '.git' in files:
            os.chdir(path)
            print os.getcwd()
            # result = os.popen('git pull')
            # print result
            os.system("git pull")

checkGit(eachPath(rootPath))
