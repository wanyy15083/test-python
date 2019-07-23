import queue
import time
from test.MySqlConn import MyPymysqlPool
import gevent
from gevent import monkey

monkey.patch_all()


#
# class QueryThread(object):
#     def __init__(self):
#         super(QueryThread, self).__init__()
#         self.q = queue.Queue()
#         self.mysql = MyPymysqlPool("mydb")
#
#     def run(self, i):
#         self.query(i)

def query(i, q):
    mysql = MyPymysqlPool("mydb")
    try:
        result = mysql.getAll("select age from person where id >= %s and id < %s",
                              [(i + 1) * 10, (i + 2) * 1000, ])
        sum = 0
        if result:
            for ret in result:
                sum += ret['age']
        q.put(sum)
    finally:
        mysql.dispose()

def query_order(i, q):
    mysql = MyPymysqlPool("harbor_prd")
    try:
        result = mysql.getAll("select loan_amount from record_loan where id >= %s and id < %s",
                              [(i + 1) * 10, (i + 2) * 1000, ])
        sum = 0
        if result:
            for ret in result:
                sum += ret['loan_amount']
        q.put(sum)
    finally:
        mysql.dispose()


if __name__ == "__main__":
    start = time.time()
    q = queue.Queue()
    jobs = []
    for i in range(5):
        # job = gevent.spawn(query, i, q)
        job = gevent.spawn(query_order, i, q)
        jobs.append(job)

    gevent.joinall(jobs)
    while not q.empty():
        print(q.get())

    # sqlAll = "select * from user;"
    # result = mysql.getAll(sqlAll)
    print("spend time:" + str(time.time() - start))
