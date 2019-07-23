import time

begin = int(time.mktime(time.strptime('2019-06-04 00:00:00', '%Y-%m-%d %H:%M:%S')))
end = int(time.mktime(time.strptime('2019-06-10 00:00:00', '%Y-%m-%d %H:%M:%S')))
while begin <= end:
    sql1 = """SELECT o.product_id,o.product_name, p.num '发起路由数',o.num '路由成功数',q.num '发起借款数' FROM (
            SELECT a.product_id, (SELECT product_name FROM config_product WHERE product_id=a.product_id) product_name, COUNT(DISTINCT a.user_gid) num FROM route_query_paras a, route_info b WHERE a.order_gid=b.order_gid AND a.create_time BETWEEN """+str(begin)+""" AND """+str(begin+36000)+""" AND b.route_state=1 GROUP BY a.product_id ) o LEFT JOIN
            (SELECT a.product_id, (SELECT product_name FROM config_product WHERE product_id=a.product_id) product_name, COUNT(DISTINCT a.user_gid) num FROM route_query_paras a WHERE a.create_time BETWEEN """+str(begin)+""" AND """+str(begin+36000)+""" GROUP BY a.product_id) p ON  o.product_id=p.product_id LEFT JOIN
            (SELECT a.product_id, (SELECT product_name FROM config_product WHERE product_id=a.product_id) product_name, COUNT(DISTINCT a.user_gid) num FROM route_query_paras a, loan_detail b WHERE a.order_gid=b.loan_gid AND a.create_time BETWEEN """+str(begin)+""" AND """+str(begin+36000)+""" AND b.withdraw_status>-1 GROUP BY a.product_id) q ON p.product_id=q.product_id;
            """
    print(sql1)
    begin = begin + 86400