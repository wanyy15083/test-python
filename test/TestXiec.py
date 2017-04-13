import gevent.monkey

gevent.monkey.patch_socket()

import gevent
import urllib2
import time


def fetch(pid):
    response = urllib2.urlopen('http://aljun.me')
    result = response.read()

    print 'Process %s : %s' % (pid,time.time())


def synchronous():
    for i in range(1, 10):
        fetch(i)


def asychronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)


print 'Synchronous:'
synchronous()

print 'Asynchronous:'
asychronous()
