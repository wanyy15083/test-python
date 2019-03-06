# -*- coding: UTF-8 -*-

import pymysql;
from DBUtils.PooledDB import PooledDB;

import test.DB_config as Config;


class ConnPool(object):
    __pool = None;

    def __enter__(self):
        self.conn = self.__getConn()
        self.cursor = self.conn.cursor()
        return self;

    def __getConn(self):
        if self.__pool is None:
            self.__pool = PooledDB(creator=pymysql, mincached=Config.DB_MIN_CACHED, maxcached=Config.DB_MAX_CACHED,
                                   maxshared=Config.DB_MAX_SHARED, maxconnections=Config.DB_MAX_CONNECYIONS,
                                   blocking=Config.DB_BLOCKING, maxusage=Config.DB_MAX_USAGE,
                                   setsession=Config.DB_SET_SESSION,
                                   host=Config.DB_TEST_HOST, port=Config.DB_TEST_PORT,
                                   user=Config.DB_TEST_USER, passwd=Config.DB_TEST_PASSWORD,
                                   db=Config.DB_TEST_DBNAME, use_unicode=False, charset=Config.DB_CHARSET)

        return self.__pool.connection()

    def __exit__(self, type, value, trace):
        self.cursor.close()
        self.conn.close()


def get_conn():
    return ConnPool()


if __name__ == '__main__':
    sql = "select * from user"
    with get_conn() as conn:
        conn.cursor.execute(sql)
        results = conn.cursor.fetchall()
        print(results)
