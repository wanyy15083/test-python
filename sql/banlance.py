import csv

with open('额度.csv') as f:
    file = csv.reader(f)
    # print(file)
    for balance in file:
        # print(balance)
        sql="update user_sub_account set current_borrowed_amount="+balance[4]+", can_borrow_amount=if("+balance[1]+"-"+balance[4]+"<0,0,"+balance[1]+"-"+balance[4]+") where user_gid='"+balance[0]+"';"
        print(sql)