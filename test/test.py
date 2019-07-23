from rediscluster import StrictRedisCluster
import sys
import pymysql


def redis_cluster():
    redis_nodes = [
        {'host': '127.0.0.1', 'port': 7000},
        {'host': '127.0.0.1', 'port': 7001},
        {'host': '127.0.0.1', 'port': 7002},
        {'host': '127.0.0.1', 'port': 7003},
        {'host': '127.0.0.1', 'port': 7004},
        {'host': '127.0.0.1', 'port': 7005}
    ]

    try:
        redis_conn = StrictRedisCluster(startup_nodes=redis_nodes)
    except Exception as e:
        print("connect error")
        sys.exit(1)

    redis_conn.set('name', 'tom')
    print("name is " + str(redis_conn.get('name'), encoding='utf-8'))


def py_mysql():
    db = pymysql.connect(host='localhost', port=3306,
                         user='root', password='1234', db='test')
    cur = db.cursor()

    sql = "select * from user"

    try:
        cur.execute(sql)
        rows = cur.fetchall()
        print("id", "name", "age", "status")
        for row in rows:
            id = row[0]
            name = row[1]
            age = row[2]
            status = row[3]
            print(id, name, age, status)
    except Exception as e:
        raise e

    sql_insert = "insert into user (name,age) values ('tom', 23)"

    try:
        cur.execute(sql_insert)
        db.commit()
    except Exception as e:
        db.rollback()

    sql_update = "update user set age = %d where name = '%s'"

    try:
        cur.execute(sql_update % (18, "tom"))
        db.commit()
    except Exception as e:
        db.rollback()

    sql_delete = "delete from user where name = ' %s'"

    try:
        cur.execute(sql_delete % ("tom"))
        db.commit()
    except Exception as e:
        db.rollback()

    db.close()

    # redis_cluster()
py_mysql()
