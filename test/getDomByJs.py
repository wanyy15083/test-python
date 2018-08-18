# -*- coding: utf-8-*-

# import os, os.path, sys
# import win32process, win32event
#
# exe_path = sys.argv[1]
# exe_file = sys.argv[2]
#
# # os.chdir(exe_path)
#
# try:
#     handle = win32process.CreateProcess(os.path.join(exe_path, exe_file), '', None, None, 0,
#                                         win32process.CREATE_NO_WINDOW, None, exe_path, win32process.STARTUPINFO())
#     running = True
# except Exception, e:
#     print "Create Errir!"
#     handle = None
#     running = False
#
# while running:
#     rc = win32event.WaitForSingleObject(handle[0], 1000)
#     if rc == win32event.WAIT_OBJECT_0:
#         running = False
#
#         # end while

import os

dir = os.getcwd()


# print dir

def get_dom(url):
    cmd = 'cmd.exe /k phantomjs.exe huaban.js "%s"' % url
    a = os.system(cmd)
    print(a)

get_dom('http://huaban.com/w1dvcnopmu/following/')