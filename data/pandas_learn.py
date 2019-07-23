from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# import pandas.io.sql as sql
# import pymysql
# config = {
#     'host': '127.0.0.1',
#     'port': 3306,
#     'user': 'root',
#     'password': '1234',
#     'db': 'test',
#     'charset': 'utf8mb4',
#     'cursorclass': pymysql.cursors.DictCursor
# }
# conn = pymysql.connect(**config)
# result = sql.read_sql("select * from person", conn)
# print(result)

# import numpy as np
# from matplotlib import pyplot as plt
#
# x = np.arange(1, 11)
# y = 2 * x + 5
# plt.title("Matplotlib demo")
# plt.xlabel("x axis caption")
# plt.ylabel("y axis caption")
# plt.plot(x, y)
# plt.show()

# comp1 = np.random.normal(0,1,size=200)
# comp2 = np.random.normal(10,2,size=200)
# values = Series(np.concatenate([comp1, comp2]))
# values.hist(bins=100,alpha=0.3,color='k',density=True)
# values.plot(kind='kde',style='k--')
# plt.show()