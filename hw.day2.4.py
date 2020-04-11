import os
s=0
for dirpath, dirames, filenames  in os.walk("d:/hudongmei"):
    for filename in filenames:
        m=os.path.join(dirpath, filename)
        size=os.path.getsize(m)
        if size>s:
            s=size
            file=filename
            path=m
print(file)
print(path)
