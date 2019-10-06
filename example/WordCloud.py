#词云
#将wordcloud库把词云当作一个wordcloud对象
import wordcloud,jieba
from imageio import imread
import matplotlib.pyplot as plt
mymask=imread(r'C:\Users\霁\Desktop\mytest\mypython\mymask.jpg')
# w=wordcloud.WordCloud(width,hight,
# min_font_size,max_font_size,font_step,font_path,
# max_words,stop_words
# mask,background_color)#maxk词云形状
f = open(r'C:\Users\霁\Desktop\mytest\mypython\123.txt',"r",encoding="utf-8")#出现一些错误，用绝对路径，文件编码要一致
txt =f.read()
f.close()
words=" ".join(jieba.lcut(txt))#将所有分词列表以空格分隔的长条文本给wordcloud对象
w = wordcloud.WordCloud(font_path = 'C:\\Users\霁\\Desktop\\mytest\\mypython\\simsun.ttc',width = 1000,height = 700,\
                        mask=mymask,background_color = 'white')
w.generate(words)#向WordCloud对象w中加载文本

plt.imshow(w)
plt.axis("off")
plt.show()
w.to_file(r"C:\Users\霁\Desktop\mytest\mypython\outfile.jpg")#将词云输出为图像文件，png等等默认宽高400px *200px
