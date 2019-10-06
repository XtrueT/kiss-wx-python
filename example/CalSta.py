#基本统计值
#获取一段不定长的数，列表
def getNum():
    num=[]
    iNumStr=input("请输入数字(回车退出)：")
    while iNumStr != "":
        num.append(eval(iNumStr))
        iNumStr = input("请输入数字(回车退出)：")
    return num
#求平均值
def avg(number):
    s=0.0
    for num in number:
        s=s+num
    return s/len(number)
#求方差
def dev(number,avg):
    sdev =0.0
    for num in number:
        sdev=sdev+(num-avg)**2
    return pow(sdev/(len(number)-1),0.5)
#中位数
def median(number):
    sorted(number)#排序
    size=len(number)
    if size%2==0:
        med=(number[size//2-1]+number[size//2])/2
    else:
        med=number[size//2]
    return med

n=getNum()
m=avg(n)
print("avg:{},dve:{:.2},median:{}".format(m,dev(n,m),median(n)))