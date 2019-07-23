import os
import json

dict = {}
with open('1.txt') as f:
    lines1 = f.readlines()
    for line in lines1:
        arr = line.split('	')
        dict[arr[0]] = arr[1].replace('\n', '')
    print(dict)

f3 = open('3.txt', 'w', encoding='utf-8')
with open('2.txt') as f:
    lines2 = f.readlines()
    for line in lines2:
        arr = line.split('\t')
        # print(arr)
        if arr[0] in dict:
            content = arr[1]
            obj = json.loads(content)
            obj['contactCode'] = dict[arr[0]]
            print(obj)
            content1 = json.dumps(obj)
            content1

            sql = "update giraffe.log_signature_info_loan set contract_code='" + dict.get(
                arr[0]) + "',contract_content='" + content1 + "', process_status= -1 where record_gid ='" + arr[
                      0] + "';"
            f3.write(sql.encode('utf-8').decode('unicode_escape') + '\n')
