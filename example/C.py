from random import random
#ImportError: cannot import name 'random' from 'random' (c:\Users\霁\Desktop\mytest\mypython\random.py)
#出现了导入异常，原来竟然是我建立了一个重名的文件在工作区里
from time import perf_counter

darts=1000*1000
hits=0.0
start=perf_counter()

for i in range(1,darts+1):
    x,y=random(),random()
    dist = pow(x**2+y**2,0.5)
    if dist <= 1.0 :
        hits += 1
pi=4*(hits/darts)
print("圆周率：{}".format(pi))
print("time:{:.5f}s".format(perf_counter()-start))