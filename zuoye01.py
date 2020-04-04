id=1
record=[]
def add_record(id):
    add_name=input("请输入姓名：")
    add_number=input("请输入电话：")
    f={"id":id,"姓名":add_name,"电话":add_number}
    record.append(f)
    print("添加成功")

def query_record():
    queryname = input("请输入要查找的姓名：")
    for i in record:
        if i["姓名"]==queryname:
            print(i)
            break
    else:
            print("不存在此人")

def change_record():
    changename = input("请输入要修改人的姓名：")
    for i in record:
        if i["姓名"]==changename:
            print("信息"
                  "1.姓名"
                  "2.电话")
            m = input("请选择要修改的信息")
            if m == "1":
                updatename = input("请输入新的姓名:")
                i["姓名"]=updatename
            elif m == "2":
                updatenumber = input("请输入新的电话:")
                i["电话"]=updatenumber
            print("修改成功")
            break
    else:
            print("不存在此人")

def delete_record():
    changename = input("请输入姓名：")
    for i in record:
        if i["姓名"]==changename:
            record.remove(i)
            print("删除成功")
    else:
        print("不存在此人")


if __name__ == "__main__":
    while 1:
        message = """
               通讯录
               1.添加
               2.查找
               3.修改
               4.删除
               5.退出
              """
        print(message)
        a = input("请选择操作：")
        if a=="1":
            add_record(id)
            id=+1
        elif a=="2":
            query_record()
        elif a=="3":
            change_record()
        elif a=="4":
            delete_record()
        elif a =="5":
            break
        else:
            print("不存在此选项")
