
import time
from test.MySqlConn import MyPymysqlPool


mysql = MyPymysqlPool("giraffe_rd")
try:
    white_list = mysql.getAll("select id,user_gid, id_card_no, capital_channel, product_ids from white_list_config")
    if white_list:
        for white in white_list:
            id = white['id']
            capital_channel = white['capital_channel']
            product_ids = mysql.getAll("select distinct a.product_id from config_product_capital_channel a, config_product b where a.product_id=b.product_id and capital_channel = %s and valid=1 and b.demander_id=1;", [capital_channel,])
            if product_ids:
                product_list = [product_id['product_id'] for product_id in product_ids]
                product_list_str = ','.join(str(product) for product in product_list)
                print(product_list_str)
                mysql.update("update white_list_config set product_ids = %s where id = %s;", [product_list_str, id,])
finally:
    mysql.dispose()