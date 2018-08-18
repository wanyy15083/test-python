# -*- coding: utf-8 -*-

import os

rootPath = '/home/bj-s2-w1631/Git/test-python/test'

paths = os.listdir(rootPath)
# dirs = os.walk(rootPath)
#
# for dir in dirs:
#     print(dir)

for path in paths:
    # print(path)
    # print(os.path.splitext(path)[1])

    if os.path.isfile(path) and os.path.splitext(path)[1] == '.py':
        print(path)
        os.system("2to3 -w "+path)


