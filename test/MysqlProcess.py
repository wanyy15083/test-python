import time
from multiprocessing import Pool, Manager
from test.MySqlConn import MyPymysqlPool


def query(q, i):
    mysql = MyPymysqlPool("mydb")
    try:
        result = mysql.getAll("select age from person where id >= %s and id < %s",
                              [(i + 1) * 10, (i + 2) * 1000, ])
        sum = 0
        if result:
            for ret in result:
                sum += ret['age']
        q.put(sum)
        return sum
    finally:
        mysql.dispose()

def query_order(q, i):
    mysql = MyPymysqlPool("harbor_prd")
    try:
        result = mysql.getAll("select loan_amount from record_loan where id >= %s and id < %s",
                              [(i + 1) * 10, (i + 2) * 1000, ])
        sum = 0
        if result:
            for ret in result:
                sum += ret['loan_amount']
        q.put(sum)
        return sum
    finally:
        mysql.dispose()


if __name__ == "__main__":
    start = time.time()

    manager = Manager()
    q = manager.Queue()
    pool = Pool(4)
    results = []
    for i in range(5):
        results.append(pool.apply_async(query_order, (q, i)))

    pool.close()
    pool.join()
    print(q.get())

    for result in results:
        print(result.get())

    # while not q.empty():
    #     print(q.get())
    # sqlAll = "select * from user;"
    # result = mysql.getAll(sqlAll)
    print("spend time:" + str(time.time() - start))
