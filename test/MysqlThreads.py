import queue
import time
from threading import Thread
from test.MySqlConn import MyPymysqlPool


class QueryThread(Thread):
    def __init__(self, i, q):
        super(QueryThread, self).__init__()
        self.i = i
        self.q = q
        self.mysql = MyPymysqlPool("mydb")
        self.harbor = MyPymysqlPool("harbor_prd")

    def run(self):
        # self.query()
        self.query_order()

    def query(self):
        try:
            result = self.mysql.getAll("select age from person where id >= %s and id < %s",
                                       [(i + 1) * 10, (i + 2) * 1000, ])
            sum = 0
            if result:
                for ret in result:
                    sum += ret['age']
            self.q.put(sum)
        finally:
            self.mysql.dispose()

    def query_order(self):
        try:
            result = self.harbor.getAll("select loan_amount from record_loan where id >= %s and id < %s",
                                  [(i + 1) * 10, (i + 2) * 1000, ])
            sum = 0
            if result:
                for ret in result:
                    sum += ret['loan_amount']
            self.q.put(sum)
        finally:
            self.harbor.dispose()


if __name__ == "__main__":
    q = queue.Queue()
    start = time.time()
    threads = []
    for i in range(5):
        query = QueryThread(i, q)
        query.start()
        threads.append(query)
    for t in threads:
        t.join()

    while not q.empty():
        print(q.get())

    # sqlAll = "select * from user;"
    # result = mysql.getAll(sqlAll)
    print("spend time:" + str(time.time() - start))
