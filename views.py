import wx 
from utils import main,kiss_dict

class MyFrame(wx.Frame):

    # 构造函数
    def __init__(self):
        #设置窗体
        #parent（为None代表为顶级窗口），注意设置父窗口后，在父窗口关闭时，子窗口也会消失
        wx.Frame.__init__(self,  parent=None,title="YWDQ",size=(700,500))
        # 将窗口放在桌面环境的中间
        self.Center()
        
        # 创建基本容器
        # panel和sizer是wxPython提供的窗口部件。是容器部件,用于存放其他窗口部件
        self.splitter = wx.SplitterWindow(self,-1)
        self.left_panel = wx.Panel(self.splitter)
        self.right_panel = wx.Panel(self.splitter)
        self.splitter.SplitVertically(self.left_panel,self.right_panel,100)
        self.splitter.SetMinimumPaneSize(200)
        list2 = []
        for item in kiss_dict.items():
            list2.append(str(item[0])+":"+item[1])
        lb2 = wx.ListBox(self.left_panel,-1,choices=list2,style=wx.LB_SINGLE) 
        #布局 
        box1 = wx.BoxSizer(wx.VERTICAL) 
        box1.Add(lb2,1,flag=wx.ALL | wx.EXPAND,border=5) 
        self.left_panel.SetSizer(box1) 


        # 创建“确定”和“取消”按钮, 并绑定事件
        self.bt_confirm = wx.Button(self.right_panel,  label='确定')
        self.bt_confirm.Bind(wx.EVT_BUTTON, self.HandleClickSubmit)
        self.bt_cancel = wx.Button(self.right_panel,  label='取消')
        self.bt_cancel.Bind(wx.EVT_BUTTON, self.HandleClickCancel)

        # 创建文本，左对齐        
        self.title = wx.StaticText(self.right_panel,  label="请输入男方姓名＆女方姓名")
        self.label_user = wx.StaticText(self.right_panel,  label="男方姓名:")
        self.text_user = wx.TextCtrl(self.right_panel,  style=wx.TE_LEFT)
        self.label_user2 = wx.StaticText(self.right_panel,  label="女方姓名:")
        self.text_user2 = wx.TextCtrl(self.right_panel,  style=wx.TE_LEFT)
        self.rs = wx.StaticText(self.right_panel,  label="ヾ(≧O≦)〃嗷~你们的gay力值会出现在这里:-O:")
        self.content=wx.StaticText(self.right_panel,label='')

        # 添加容器，容器中控件按横向并排排列
        # proportion是表示当前窗口大小发生改变时，控件之间的比例
        # flag表示窗口风格，对齐方式，边框等信息
        # border边框大小（前提是flag设置了边框）
        # userdata用于传递额外的数据
        sizer_user = wx.BoxSizer(wx.HORIZONTAL)
        sizer_user.Add(self.label_user,  proportion=0,  flag=wx.ALL,  border=5)
        sizer_user.Add(self.text_user,  proportion=1,  flag=wx.ALL,  border=5)

        sizer_user2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_user2.Add(self.label_user2,  proportion=0,  flag=wx.ALL,  border=5)
        sizer_user2.Add(self.text_user2,  proportion=1,  flag=wx.ALL,  border=5)

        sizer_content= wx.BoxSizer(wx.HORIZONTAL)
        sizer_content.Add(self.rs,  proportion=1,  flag=wx.ALIGN_CENTER,  border=5)
        sizer_content.Add(self.content,  proportion=1,  flag=wx.ALIGN_CENTER,  border=5)

        sizer_button = wx.BoxSizer(wx.HORIZONTAL)
        sizer_button.Add(self.bt_confirm,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)
        sizer_button.Add(self.bt_cancel,  proportion=0,  flag=wx.ALIGN_CENTER,  border=5)

        # 添加容器，容器中控件按纵向并排排列
        box2 = wx.BoxSizer(wx.VERTICAL)
        box2.Add(self.title,  proportion=0,  flag=wx.BOTTOM | wx.TOP | wx.ALIGN_CENTER, border=15)
        box2.Add(sizer_user,  proportion=0,  flag=wx.EXPAND | wx.LEFT | wx.RIGHT,  border=45)
        box2.Add(sizer_user2,  proportion=0,  flag=wx.EXPAND | wx.LEFT | wx.RIGHT,  border=45)
        box2.Add(sizer_button,  proportion=0,  flag=wx.ALIGN_CENTER | wx.TOP,  border=15)
        box2.Add(sizer_content,1,flag=wx.ALL|wx.EXPAND,border=5)
        self.right_panel.SetSizer(box2)



    # 事件处理
    # 点击确定按钮，执行方法
    def HandleClickSubmit(self, event):
        message = ""
        name1 = self.text_user.GetValue()
        name2 = self.text_user2.GetValue() 
        if name1 == "" and name2 == "":   
            message = '不能为空'
            wx.MessageBox(message) 
        elif name1=="":
            message = '男方姓名不能为空'
            wx.MessageBox(message) 
        elif name2=="":
            message = '女方姓名不能为空'
            wx.MessageBox(message)
        else:
            message = main(name1,name2)
            print(message)
        list=["不能为空","男方姓名不能为空","女方姓名不能为空"]
        if message not in list:
            self.content.SetLabel(message)


    # 没有event点击取消会报错
    def HandleClickCancel(self, event):  
        self.text_user.SetValue("")                              
        self.text_user2.SetValue("") 
