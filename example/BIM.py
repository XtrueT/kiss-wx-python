# guess=eval(input())
# #紧凑形式 2分支 <表达式1> if <判断条件> else <表达式2>
# print("猜{}了".format("对" if guess==99 else "错"))
height,weight=eval(input("输入身高，体重（逗号隔开）："))
bmi=weight/pow(height,2)
print("BMI:{:.2f}".format(bmi))
who=""
if bmi<18.5:
    who="偏瘦"
elif 18.5<=bmi<25:
    who="正常"
elif 25<=bmi<30:
    who="偏胖"
else:
    who="肥胖"
print("BMI :{}".format(who))