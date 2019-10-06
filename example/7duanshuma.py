#7段数码管时间
import turtle,time
def drawGap():#绘制数码管间隔
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):#绘制单段数码管,设置draw取真假值,以中线左端为起点
    drawGap()
    turtle.pendown() if draw else turtle.penup()#如果darw为真，画笔落下，否则不落直接飞过去40px
    turtle.fd(40)#行进40px
    drawGap()
    turtle.right(90)#转向右90度
def drawDigit(digit):#根据数字绘制,0<digit<9
    drawLine(True) if digit in [2,3,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,6,8] else drawLine(False)
    turtle.left(90)#回到起点向左转90度
    drawLine(True) if digit in [0,4,5,6,8,9] else drawLine(False)
    drawLine(True) if digit in [0,2,3,5,6,7,8,9] else drawLine(False)
    drawLine(True) if digit in [0,1,2,3,4,7,8,9] else drawLine(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20)#移动到另一个位置绘制数字
def drawDate(date):#获得要输出的数字
    for i in date:
        if i=='-':
            turtle.penup()
            turtle.right(90)
            turtle.fd(30)
            turtle.write('年',font=("Arial",48,"normal"))
            turtle.pencolor("green")
            turtle.left(180)
            turtle.fd(30)
            turtle.right(90)
            turtle.fd(70)
        elif i=='=':
            turtle.penup()
            turtle.right(90)
            turtle.fd(30)
            turtle.write('月',font=("Arial",48,"normal"))
            turtle.pencolor("blue")
            turtle.left(180)
            turtle.fd(30)
            turtle.right(90)
            turtle.fd(70)
        elif i=='+':
            turtle.penup()
            turtle.right(90)
            turtle.fd(30)
            turtle.write('日',font=("Arial",48,"normal"))
            turtle.left(180)
            turtle.fd(30)
            turtle.right(90)
            turtle.fd(70)
        else:
            drawDigit(eval(i))#用eval()将数字变为整数
def main():
    turtle.setup(1000,350,150,150)
    turtle.pencolor('red')
    turtle.penup()
    turtle.fd(-450)
    turtle.pensize(5)
    t=time.gmtime()
    timeStr=time.strftime("%Y-%m=%d+",t)
    drawDate(timeStr)
    turtle.hideturtle()
    turtle.done()
main()        