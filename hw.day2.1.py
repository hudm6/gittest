class login():
    def __init__(self):
        self.username = input("请输入用户名:")
        self.passwd = input("请输入密码:")

def permit(func):
    def wrapper():
        info=login()
        if info.username == 'root' and info.passwd == '1223':
            print('你有权限')
            return func()
        else:
            print('你没有权限')
            return
    return wrapper

@permit
def test1():
    data = "1,2,3"
    print(data)

@permit
def test2():
    data = "4,5,6"
    print(data)

test1()
test2()