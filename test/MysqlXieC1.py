import queue
import time
import decimal
import test.DB_pool as pool
import gevent
from gevent import monkey

monkey.patch_all()


def query(q, sql_loan, pos, pos_end, id):
    try:
        db_start = time.time()
        account_sum = {}
        with pool.get_conn().cursor() as cursor:
            cursor.execute(sql_loan, (pos, pos_end, id['id']))
            loan_sum = cursor.fetchone()
            print(ids)
            result = loan_sum['loan_sum']
            account_sum[id] = result
            print("account_id:%d, cost time:%s" % (id['id'], str(time.time() - db_start)))
        q.put(account_sum)
    finally:
        pool.get_conn().__exit__()


if __name__ == "__main__":
    start = time.time()
    try:
        with pool.get_conn().cursor() as cursor:
            sql_account = "SELECT id FROM config_account WHERE valid=1"
            sql_loan = "SELECT SUM(a.loan_sum) loan_sum FROM loan_detail a JOIN account_order b ON a.loan_gid = b.order_gid WHERE a.create_time BETWEEN %s AND %s AND a.withdraw_status IN(-2, 0, 1, 9) AND b.account_id = %s"

            cursor.execute(sql_account)
            ids = cursor.fetchall()
            print(ids)
            start = int(time.mktime(time.strptime('2018-08-16 00:00:00', "%Y-%m-%d %H:%M:%S")))
            end = int(time.mktime(time.strptime('2018-08-16 23:59:59', "%Y-%m-%d %H:%M:%S")))

            start_time = start
            end_time = end
            div = (end_time - start_time) / 3600
            rem = (end_time - start_time) % 3600
            num = div if rem == 0 else div + 1

            total_start = time.time()
            q = queue.Queue()
            jobs = []
            id_list = []
            for id in ids:
                id_list.append(id['id'])
                pos = start
                for i in range(int(num)):
                    pos_end = pos + 3600 - 1
                    if pos_end > end:
                        pos_end = end
                    job = gevent.spawn(query, q, sql_loan, pos, pos_end, id['id'])
                    jobs.append(job)

            gevent.joinall(jobs)

            result_id = {}
            while not q.empty():
                print(q.get())
                for id in id_list:
                    v = result_id[id['id']]
                    if v:
                        if q.get()[id] == id:
                            result_id[id] = v + q.get()[id]
                    else:
                        result_id[id] = decimal(0)

            for id in id_list:
                print("account_id:%d, sum:%s" % (id, result_id[id]))

            print("total time:" + str(time.time() - total_start))

    finally:
        pool.get_conn().__exit__()
