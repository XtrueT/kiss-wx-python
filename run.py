import wx
from views import MyFrame

if __name__ == '__main__':
    # 初始化
    app = wx.App()
    # 实例MyFrame类，并传递参数 
    frame = MyFrame()
    # 显示窗口    
    frame.Show()
    # 调用主循环方法                        
    app.MainLoop()                      
