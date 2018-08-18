from twisted.internet import defer, reactor, task
from twisted.web.client import getPage

maxRun = 2

urls = ['http://zhaiduixueshe.com', 'http://baidu.com', 'http://taobao.com']


def pageCallbake(res):
    print(len(res))
    return res


def doWork():
    for url in urls:
        d = getPage(url)
        d.addCallback(pageCallbake)
        yield d


def finish(ign):
    reactor.stop()


def test():
    defereds = []
    coop = task.Cooperator()
    work = doWork()
    for i in range(maxRun):
        d = coop.coiterate(work)
        defereds.append(d)
    dl = defer.DeferredList(defereds)
    dl.addCallback(finish)


test()
reactor.run()
