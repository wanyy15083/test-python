import re

data = []
with open('log.txt') as f:
    lines = f.readlines()
    for line in lines:
        result = re.findall("orderGid='.*?'", line)
        print(result)
    print(data)