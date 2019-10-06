#玫瑰花
import turtle as t
#曲线函数
def Degreecurve(n,r, d=1):
    for i in range(n):
        t.left(d)
        t.circle(r,abs(d))

def Rose_Setup(x,y):
    return t.setup(x,y)

def Rose_pencolor(color):
    return t.pencolor(color)

def Rose_fillcolor(color):
    return t.fillcolor(color)

def Rose_speed(s):
    return t.speed(s)

def Rose_goto(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def Rose_circle(c,r):
    return t.circle(c,r)

def Rose_fd(s):
    return t.fd(s)

def Rose_left(s):
    return t.left(s)

def Rose_right(s):
    return t.right(s)

def Rose_begin():
    return t.begin_fill()

def Rose_end():
    return t.end_fill()

def Rose_rt(s):
    return t.rt(s)
#初始位置设定
def adr(s):
    Rose_Setup(450*5*s,750*5*s)
    Rose_pencolor("black")
    Rose_fillcolor("blue")
    Rose_speed(100)
    Rose_goto(0,900*s)
#花朵
def rose_xz(s):
    Rose_begin()
    Rose_circle(200*s,30)
    Degreecurve(60,50*s)
    Rose_circle(200*s,30)
    Degreecurve(4,100*s)
    Rose_circle(200*s,50)
    Degreecurve(50,50*s)
    Rose_circle(350*s,65)
    Degreecurve(40,70*s)
    Rose_circle(150*s,50)
    Degreecurve(20,50*s,-1)
    Rose_circle(400*s,60)
    Degreecurve(18,50*s)
    Rose_fd(250*s)
    Rose_right(150)
    Rose_circle(-500*s,12)
    Rose_left(140)
    Rose_circle(550*s,110)
    Rose_left(27)
    Rose_circle(650*s,100)
    Rose_left(130)
    Rose_circle(-300*s,20)
    Rose_right(123)
    Rose_circle(220*s,57)
    Rose_end()
#花枝
def rose_hz(s):
    Rose_left(120)
    Rose_fd(280*s)
    Rose_left(115)
    Rose_circle(300*s,33)
    Rose_left(180)
    Rose_circle(-300*s,33)
    Degreecurve(70,225*s,-1)
    Rose_circle(350*s,104)
    Rose_left(90)
    Rose_circle(200*s,105)
    Rose_circle(-500*s,63)
    Rose_goto(170*s,-30*s)
    Rose_left(160)
    Degreecurve(20,2500*s)
    Degreecurve(220,250*s,-1)

#叶子
def rose_yz(s):
    Rose_fillcolor("green")
    Rose_goto(670*s,-180*s)
    Rose_right(140)
    Rose_begin()
    Rose_circle(300*s,120)
    Rose_left(60)
    Rose_circle(300*s,120)
    Rose_end()
    Rose_goto(180*s,-550*s)
    Rose_right(85)
    Rose_circle(600*s,40)
    Rose_goto(-150*s,-1000*s)
    Rose_begin()
    Rose_rt(120)
    Rose_circle(300*s,115)
    Rose_left(75)
    Rose_circle(300*s,100)
    Rose_end()
    Rose_goto(430*s,-1070*s)
    Rose_right(30)
    Rose_circle(-600*s,35)

def main(s):
    adr(s)
    rose_xz(s)
    rose_hz(s)
    rose_yz(s)

main(0.1)
t.hideturtle()
t.done()

