import os

home = "/home/songyigui/"

dirs = os.listdir(home)
print(dirs)
i =1
for dir in dirs:
    # i+=1
    if os.path.isdir(home+dir):
        if dir == '.npm':
            os.system('tar cvpzf '+dir.replace('.','')+'.tgz --exclude=/home/songyigui/.gradle --exclude=/home/songyigui/.m2 --exclude=/home/songyigui/.deepinwine  '+'/home/songyigui/'+dir)



# for root,dir,file in os.walk(home):
    # print(root)
    # print(dir)
    # print(file)