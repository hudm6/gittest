# 作业1：使用多线程写一个并发http，get请求的程序，可设置并发数和请求总数，返回请求状态码

#方法一：
import threading,queue
import requests
import time

requestnum=100
bfnum=5

lock=threading.Lock()
dataQueue = queue.Queue()

url="http://www.baidu.com"

def producer():
        dataQueue.put(i)

def consumer():
        while True:
            try:
                data = dataQueue.get(block=False)
            except queue.Empty:
                break
            a=requests.get(url)
            time.sleep(1)
            with lock:
                print(a.status_code)
                dataQueue.task_done()
if __name__ == '__main__':
    for i in range(requestnum):
        t = threading.Thread(target=producer)
        t.start()

    for i in range(bfnum):
        thread = threading.Thread(target=consumer)
        thread.start()

    dataQueue.join()

#方法二：
import threading, queue
import requests
import time

maxThreads = 5
requestnum = 100

url = "http://www.baidu.com"
lock = threading.Lock()

def consumer(dataQueue):
    a = requests.get(url)
    time.sleep(1)
    with lock:
        print(a.status_code)
        dataQueue.get()
    dataQueue.task_done()


def main():
    dataQueue = queue.Queue(maxThreads)
    for s in range(requestnum):
        dataQueue.put(s)
        thread = threading.Thread(target=consumer,args=(dataQueue,))
        thread.start()
    dataQueue.join()

if __name__ == '__main__':
    main()


# 作业2:使用多进程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码

from multiprocessing import Pool
import time
import requests

url="http://www.baidu.com"
def func(num):
        a=requests.get(url)
        time.sleep(1)
        print(a.status_code)

if __name__ == '__main__':
    pool = Pool(processes=5)
    for i in range(20):
        pool.apply_async(func, (i,))
    pool.close()
    pool.join()


# 作业3：get和post方法的区别

"""1.get使用url或者cookie传参，而post将数据放在body中
2.get的url会有长度上的限制，则post的数据则可以非常大
3.post比get安全，因为数据在地址栏上不可见
4.一般get请求用来获取数据，post请求用来发送数据
5.GET请求参数会被完整保留在浏览器历史记录里，而POST中的参数不会被保留。
6.GET请求只能进行url编码，而POST支持多种编码方式。"""

# 作业4. post请求有哪几种数据格式
"""
1.application/x-www-form-urlencoded
2.multipart/form-data
3.application/json
4.text/xml
"""
