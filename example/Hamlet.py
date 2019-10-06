#哈姆雷特统计
def getText():
    txt=open(r"wxPython_Kiss\assets\Hamlet.txt","r",encoding="utf-8").read()
    txt=txt.lower()
    for ch in '!"@#$%&()+-*/,.:;<=>?[\\]^_‘{|}~':
        txt=txt.replace(ch," ")
    return txt
hamletTxt=getText()
words=hamletTxt.split()
counts={}
for word in words:
    counts[word]=counts.get(word,0)+1#是0则+1=1所以相当于加了一对键值对
items=list(counts.items())#元组对应的一个列表项
items.sort(key=lambda x:x[1],reverse=True)
#默认从小到大，使用reverse=True让其返回从大到小，
#前面的key=lambda x:x[1]则是让其排序使用count值进行排序，即选择多元列表里的第2个，如：[(li,2)]选取2
for i in range(10):
    word,count=items[i]#将排序好的列表项的键值对分别赋值
    print("{0:<20} {1:>5}".format(word,count))
