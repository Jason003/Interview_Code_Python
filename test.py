# def _private1():
# 	return "jason"
# def _private2():
# 	return "lee"
# def greeting():
# 	print("hello " + _private1() + " " + _private2())
# s = '0'
# n = int(s)
# print(20 / n)

# with open("1.txt","a") as f:
	# for l in f.readlines():
		# print(l)
	# print(f.read())
	# f.write("dawqd")
# from io import BytesIO
# f = BytesIO()
# f.write("李捷繁".encode("utf-8"))
# print(f.getvalue())

# import json
# d = dict(name = "jason", age = 21)
# print(json.dumps(d))

# import multiprocessing 
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = multiprocessing.Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')


# import subprocess
# r = subprocess.call(["nslookup", "www.python.org"])

# from multiprocessing import Process, Queue
# import os, time, random

# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())

# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)

# if __name__=='__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#     # 等待pw结束:
#     pw.join()
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# import threading, time
# def loop1():
# 	print("thread %s is running" %threading.current_thread().name)
# 	time.sleep(2)
# def loop2():
# 	print("thread %s is running" %threading.current_thread().name)
# 	time.sleep(2)


# print("thread %s is running" %threading.current_thread().name)
# threading.Thread(target=loop1, name="threadLoop1").start()
# threading.Thread(target=loop2, name="threadLoop2").start()

# import multiprocessing
# from multiprocessing import Pool, Process
# import threading

# def loop(i):
#     x = 0
#     print('Thread - ',i)
#     while True:
#         x = x ^ 1

# def proc(i, cpu_cout):
#     print('Process: ',i)
#     for i in range(cpu_cout*2):
#         t = threading.Thread(target=loop, args=(i,))
#         t.start()

# if __name__ == '__main__':
#     cpu_cout = multiprocessing.cpu_count()
#     p = Pool(cpu_cout)
#     for i in range(cpu_cout):
#         p.apply_async(proc,args=(i, cpu_cout))
#     p.close()
#     p.join()

# import time, threading

# # 假定这是你的银行存款:
# balance = 0

# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#         change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)

# import time, threading

# # 假定这是你的银行存款:
# balance = 0
# lock = threading.Lock()
# def change_it(n):
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     for i in range(100000):
#     	lock.acquire()
#     	try:
#     		change_it(n)
#     	except Exception as e:
#     		raise e
#     	finally:
#     		# pass
#     		lock.release()
# while balance == 0:
# 	t1 = threading.Thread(target=run_thread, args=(5,))
# 	t2 = threading.Thread(target=run_thread, args=(8,))
# 	t1.start()
# 	t2.start()
# 	t1.join()
# 	t2.join()
# print(balance)

# import threading

# # 创建全局ThreadLocal对象:
# local_school = threading.local()

# def process_student(std):
#     # 获取当前线程关联的student:
#     # std = local_school.student
#     print('Hello, %s (in %s)' % (std, threading.current_thread().name))

# def process_thread(name):
#     # 绑定ThreadLocal的student:
#     # local_school.student = name
#     process_student(name)

# t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
# t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# import re
# print(re.match(r'^\d{3}\-\d{3,8}$', "12331341"))
# print(re.split(r"[\s\,\;]+", "a a a    aa     , ,  "))
# m = re.match(r"^(\d{3})-(\d{3,8}?)(\d*)$", "010-21231")
# tel = re.compile(r"^(\d{3})-(\d{3,8}?)(\d*)$")
# m = tel.match("222-21214141")
# print(m.group(1))
# print(m.group(2))
# print(m.group(3))

# email = re.compile(r"^[a-zA-Z]+[.]?[a-zA-Z]+@[a-zA-Z]+\.com$"))
# print(email.match("mr-bob@example.com"))

# from datetime import datetime
# dt = datetime.now()
# print(dt.timestamp())

# import collections
# q = collections.deque([1,2,3,4,5])
# q.appendleft(1)
# q.popleft()
# print(q)

# Circle = collections.namedtuple("Circle", ('x', 'y', 'r'))
# c1 = Circle(1,2,3)
# print(c1)


# from urllib import request
# req = request.Request('http://www.douban.com/')
# req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print('Data:', data.decode('utf-8'))

# import requests
# r = requests.get("https://www.douban.com/")
# print(r.text)

# from tkinter import *
# class Application(Frame):
# 	def __init__(self, master = None):
# 		Frame.__init__(self, master)
# 		self.pack()
# 		self.createWidgets()
# 	def createWidgets(self):
# 		self.helloLabel = Label(self, text = "Hello, world!")
# 		self.helloLabel.pack()
# 		self.quitButton = Button(self, text='Quit', command=self.quit)
# 		self.quitButton.pack()
# app = Application()
# app.master.title('Hello World')
# app.mainloop()

# from tkinter import *
# import tkinter.messagebox as messagebox

# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()

#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)

# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()

# 导入turtle包的所有内容:
# from turtle import *

# # 设置笔刷宽度:
# width(4)

# # 前进:
# forward(200)
# # 右转90度:
# right(90)

# # 笔刷颜色:
# pencolor('red')
# forward(100)
# right(90)

# pencolor('green')
# forward(200)
# right(90)

# pencolor('blue')
# forward(10)
# right(90)

# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
# done()

from turtle import *

# 设置色彩模式是RGB:
colormode(255)

lt(90)

lv = 14
l = 120
s = 45

width(lv)

# 初始化RGB颜色:
r = 0
g = 0
b = 0
pencolor(r, g, b)

penup()
bk(l)
pendown()
fd(l)

def draw_tree(l, level):
    global r, g, b
    # save the current pen width
    w = width()

    # narrow the pen width
    width(w * 3.0 / 4.0)
    # set color:
    r = r + 1
    g = g + 2
    b = b + 3
    pencolor(r % 200, g % 200, b % 200)

    l = 3.0 / 4.0 * l

    lt(s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    rt(2 * s)
    fd(l)

    if level < lv:
        draw_tree(l, level + 1)
    bk(l)
    lt(s)

    # restore the previous pen width
    width(w)

speed("fastest")

draw_tree(l, 4)

done()