#递归求解 n!
def myfact(n):
    if n==0:
        return 1
    else:
        return n*myfact(n-1)
print(myfact(3))
#递归实现字符串反转
def myfact1(s):
    if s=="":
        return s
    else:
        return myfact1(s[1:])+s[0]
print(myfact1("123456789"))
#斐波那契数列
def myfact2(n):
    if n==1 or n==2:
        return 1
    else:
        return myfact2(n-1)+myfact2(n-2)
print(myfact2(4))        
#汉诺塔问题
count=0
def myfact3(n,src,dst,mid):
#n个圆盘，src:原来柱子，dst:目标柱子 ,mid：中间柱子
    global count
    if n==1:
        print("{}:{}->{}".format(1,src,dst))
        count+=1
    else:
        myfact3(n-1,src,mid,dst)
        print("{}:{}->{}".format(n,src,dst))
        count+=1
        myfact3(n-1,mid,dst,src)
myfact3(3,"A","C","B")#3个圆盘，A移到 C
print(count)

