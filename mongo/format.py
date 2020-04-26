dict = {}
with open('data.txt') as f:
    lines = f.readlines()
    for line in lines:
        arr = line.split(':')
        sql = 'db.getCollection("packet_dict").insert({' \
                'key: "' + arr[0][0:5] + '_' + arr[0][6:arr[0].index(')')] + '",'\
                'value: ' + arr[1].rstrip() + ','\
                'gmtCreate: ISODate("2020-04-25T11:02:36.921Z"),'\
                'gmtUpdate: ISODate("2020-04-25T11:02:36.921Z")'\
            '});'
        print(sql)
