#体育竞技分析
from random import random
#打印介绍内容
def Info():
    print("这个程序模拟2个选手的某种竞技比赛")
    print("程序运行需要A,B能力值（0-1）")
#获得能力值
def getInput():
    a=eval(input("输入A的能力值："))
    b=eval(input("输入B的能力值："))
    n=eval(input("输入比赛的场次："))
    return a,b,n
#比赛结束规则 15分一局
def gameOver(a,b):
    return a==15 or b==15
#模拟一局比赛
def simOnegames(porbA,porbB):
    scoreA,scoreB=0,0
    serving="A"
    while not gameOver(scoreA,scoreB):
        if serving=="A":
            if random()<porbA:
                scoreA+=1
            else:
                serving="B"
        else:
            if random()<porbB:
                scoreB+=1
            else:
                serving="A"
    return scoreA,scoreB
#模拟n局比赛
def simNgames(n,porbA,porbB):
    winA,winB=0,0
    for i in range(n):
        scoreA,scoreB=simOnegames(porbA,porbB)
        if scoreA>scoreB:
            winA+=1
        else:
            winB+=1
    return winA,winB
#打印相关场数结果
def Psummary(winA,winB):
    n=winA+winB
    print("竞技分析开始一共模拟{}场比赛".format(n))
    print("A获胜{},占比{:0.1%}".format(winA,winA/n))
    print("B获胜{},占比{:0.1%}".format(winB,winB/n))        
def main():
    Info()
    porbA,porbB,n=getInput()
    winA,winB=simNgames(n,porbA,porbB)
    Psummary(winA,winB)
main()
