import os

# 结果定义
kiss_dict = {
        0:"亲密无间",
        1:"永远和你在一起",
        2:"水火不兼容",
        3:"知心朋友",
        4:"心上人",
        5:"帮你做事的人",
        6:"帮你的人",
        7:"面和心不合",
        8:"男女关系不正常",
        9:"情投意合",
        10:"关系马虎"
}

# 获取名字转换成列表
def getNameList(name): 
    return list(name)


# 获取单个字符unicode对应的笔划数
def getStroke(c):
    strokes = []
    # 获取文件路径以程序运行的绝对路径添加
    # 防止打包后运行时寻找不到文件
    app_path = os.path.abspath('.')
    print(os.path.normpath(app_path+'\\assets\\strokes.txt'))
    file_path = os.path.normpath(app_path+'\\assets\\strokes.txt') 
    with open(file_path, 'r') as fr:
        for line in fr:
            strokes.append(int(line.strip()))
    unicode_ = ord(c)
    if 13312 <= unicode_ <= 64045:
        return strokes[unicode_-13312]
    elif 131072 <= unicode_ <= 194998:
        return strokes[unicode_-80338]
    else:
        return 'ERROR'


# 获取名字列表,返回一个笔划数列表
def getNameStrokes(name_list):
    stroke_list = []
    for i in range(len(name_list)):
        stroke_list.append(getStroke(name_list[i]))
    return stroke_list


# 获取2个笔划列表,整合成一个交叉的列表
def newList(one_list,two_list):
    temp_list = one_list
    i = 1
    for item in two_list:
        temp_list.insert(i,item)
        i += 2
    return temp_list


# 递归计算最后的结果
def FactResult(new_list):
    try:
        if len(new_list) == 1:
            return new_list[0]
        else:
            rs_list = []
            for i in range(len(new_list) - 1):
                a = abs(new_list[i] - new_list[i+1])
                rs_list.append(a)
            return FactResult(rs_list)
    except TypeError:
        return 'Error'


# 调用方法
def main(b_name,g_name):
    b_name_list = getNameList(b_name)
    g_name_list = getNameList(g_name)
    new_list = newList(getNameStrokes(b_name_list),getNameStrokes(g_name_list))
    return kiss_dict.get(FactResult(new_list),"不存在")