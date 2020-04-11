import os
dirpath="d:\hudongmei"
s=0
for i in os.listdir(dirpath):
    m=os.path.join(dirpath, i)
    if os.path.isfile(m):
        size=os.path.getsize(m)
        if size>s:
            s=size
            file=i
            path=m
print(file)
print(path)