import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import numpy
import numpy as np


class Application(tk.Frame):
    def __init__(self,root):
        super().__init__(root)


        ##解决matlib报错
        matplotlib.use('qt5agg')
        self.master = root

        #功能参数
        self.select = tk.StringVar()

        #一元函数
        self.one_k = tk.StringVar()
        self.one_b = tk.StringVar()

        #二元函数
        self.two_a = tk.StringVar()
        self.two_b = tk.StringVar()
        self.two_c = tk.StringVar()

        #二维码字符串
        self.str_para = tk.StringVar()


        self.pack()
        self.envar= tk.StringVar(None,"123")
        root.geometry('500x400')
        root.title("画图")
        self.int_window()

    def Buttonclick(self):
        self.select.set(self.selector.get())
        print(self.select.get())
        if self.select.get() == "一元函数":
            print("一元函数绘图")
            one_k = self.one_k.get()
            one_b = self.one_b.get()
            if len(one_k)==0 or len(one_b)==0:
                messagebox.showinfo("提示"," 请输入正确信息")
                return
            # messagebox.showinfo("提示","你输入的账号为:%s\n密码为：%s" %(u,p))
            x = np.linspace(-1 ,1 , 50)
            y= int(one_k) * x +int(one_b)
            plt.plot(x,y)
            plt.show()
            return
        if self.select.get() == "二元函数":
            print("二元函数绘图")
            two_a  = self.two_a.get()
            two_b  = self.two_b.get()
            two_c  = self.two_c.get()
            if len(two_a)==0 or len(two_b)==0 or len(two_c)==0:
                messagebox.showinfo("提示"," 请输入正确信息")
                return
            # messagebox.showinfo("提示","你输入的账号为:%s\n密码为：%s" %(u,p))
            x = np.linspace(-1 ,1 , 50)
            y= int(two_a) * x **2 + int(two_b) * x + int(two_c)
            plt.plot(x, y)
            plt.show()
            return

    def selector_listener(self, *args):
        self.select.set(self.selector.get())
        print(self.select.get())

    def int_window(self):
        # ##标签
        # tk.Label(self,text=123,fg='red',bg='green',width=6).grid(row=0,column=0)
        # tk.Entry(self,textvariable =self.envar,fg='#ff9',bg='#325',width=5).grid(row=0,column=1)
        # text = tk.Text(self,fg="#231",bg="#578",width=12)
        # text.grid(columnspan=2,rowspan=2,ipadx=50,ipady=50)
        # text.insert("end","12432")
        # text.insert("1.1", "ooooooooo")
        ##frame管理
        frame1= tk.Frame(self)
        frame2=tk.Frame(self)
        frame3=tk.Frame(self)
        #一元函数
        tk.Label(frame1,text="k",width=1).grid(row=1,column=0)
        tk.Entry(frame1,textvariable=self.one_k).grid(row=1,column=1)
        tk.Label(frame1,text="b",width=1).grid(row=1,column=2)
        tk.Entry(frame1,textvariable=self.one_b).grid(row=1,column=3)
        #二元函数
        tk.Label(frame1,text="a").grid(row=2,column=0)
        tk.Entry(frame1,textvariable=self.two_a).grid(row=2,column=1)
        tk.Label(frame1,text="b").grid(row=2,column=2)
        tk.Entry(frame1,textvariable=self.two_b).grid(row=2,column=3)
        tk.Label(frame1,text="c").grid(row=2,column=4)
        tk.Entry(frame1,textvariable=self.two_c).grid(row=2,column=5)

        #二维码字符串
        tk.Label(frame1,text="字符串", width=6).grid(row=3,column=0)
        tk.Entry(frame1,textvariable=self.str_para).grid(row=3,column=1)

        tk.Label(frame1,text="功能选择").grid(row=0,column=0)
        self.selector = ttk.Combobox(frame1,values=("一元函数","二元函数","二维码生成"),width="15")
        self.selector.grid(row=0,column=1)
        self.selector.current(0)
        self.selector.bind("<<ComboboxSelected>>", self.selector_listener)

        # self.selector["values"]= (1,2)

        # frame3.grid(pady=15)
        frame1.grid(pady=15)
        # frame2.grid(pady=15)

        #Button
        button=tk.Button(self,text="运行图像",width=15,command=self.Buttonclick)
        button.grid(padx=5)

        ##控件属性配置和获取
        # button["text"]="1111"

        ##移除控件，去掉位置参数
        # button.grid_forget()
        # #隐藏控件
        # button.grid_remove()
        # ##重新建立
        # button.grid()
        # ##固定控件
        # button.grid_propagate(0)
        ##剪贴板操作
        # self.clipboard_append("123")#剪贴板里加东西
        # self.clipboard_get()#获取剪贴板
        # self.clipboard_clear()#清空剪贴板

if __name__ == '__main__':
    root = tk.Tk()
    application = Application( root = root )
    application.mainloop()


