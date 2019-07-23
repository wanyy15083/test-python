import queue
import time
from test.MySqlConn import MyPymysqlPool
import asyncio
import logging

async def query(i):
    mysql = MyPymysqlPool("mydb")
    try:
        result = mysql.getAll("select age from person where id >= %s and id < %s",
                              [(i + 1) * 10, (i + 2) * 1000, ])
        sum = 0
        if result:
            for ret in result:
                sum += ret['age']
        return sum
    finally:
        mysql.dispose()

async def query_order(i):
    mysql = MyPymysqlPool("harbor_prd")
    try:
        result = mysql.getAll("select loan_amount from record_loan where id >= %s and id < %s",
                              [(i + 1) * 10, (i + 2) * 1000, ])
        sum = 0
        if result:
            for ret in result:
                sum += ret['loan_amount']
        return sum
    finally:
        mysql.dispose()

async def main():
    start = time.time()
    jobs = []
    for i in range(5):
        job = asyncio.create_task(query_order(i))
        jobs.append(job)
    await asyncio.gather(*jobs)
    for job in jobs:
        print(job.result())
    print("spend time:" + str(time.time() - start))

asyncio.run(main())

# if __name__ == "__main__":
#     logging.basicConfig(level=logging.DEBUG)
#     start = time.time()
#     jobs = []
#
#     for i in range(5):
#         # job = asyncio.ensure_future(query(i))
#         # job = asyncio.ensure_future(query_order(i))
#         job = asyncio.create_task(query_order(i))
#         # job = query(i, q)
#         jobs.append(job)
#
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(asyncio.wait(jobs))
#     asyncio.run(asyncio.wait(jobs))
#     for job in jobs:
#         print(job.result())
#
#     print("spend time:" + str(time.time() - start))
