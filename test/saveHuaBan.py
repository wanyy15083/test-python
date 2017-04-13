# -*- coding:utf-8 -*-

import pymysql

config = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': '1234',
    'db': 'test',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}


class HuabanMysql():
    def __init__(self):
        try:
            self.conn = pymysql.connect(**config)
            self.cursor = self.conn.cursor()
        except pymysql.Error, e:
            print 'fail to connect mysql:%s' % e.message

    def save_data(self, table, my_dict):
        cols = ','.join(my_dict.keys())
        values = '","'.join(my_dict.values())
        sql = 'insert into %s (%s) values (%s)' % (table, cols, '"' + values + '"')
        try:
            self.cursor.execute(sql)
            self.conn.commit()
        finally:
            self.conn.close()
