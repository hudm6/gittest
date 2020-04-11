import os
filelist = []
def a(dirpath):
    for i in os.listdir(dirpath):
        m=os.path.join(dirpath,i)
        if os.path.isfile(m):
            filelist.append(i)
        else:
            a(m)

if __name__ == "__main__":
    a("d:\hudongmei")
    print (filelist)


