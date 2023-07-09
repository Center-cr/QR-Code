import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class Application(tk.Frame):
    def __init__(self,root):
        super().__init__(root)
        self.master = root
        self.username=tk.StringVar()
        self.password=tk.StringVar()
        self.pack()
        self.envar= tk.StringVar(None,"123")
        root.geometry('300x200')
        root.title("登陆界面")
        self.int_window()
        self.select = tk.StringVar()
    def Buttonclick(self):
        u=self.username.get()
        p=self.password.get()
        if len(u)==0 or len(p)==0:
            messagebox.showinfo("提示"," 请输入正确信息")
            return
        messagebox.showinfo("提示","你输入的账号为:%s\n密码为：%s" %(u,p))
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
        tk.Label(frame1,text="账号").grid(row=0,column=0)
        tk.Entry(frame1,textvariable=self.username).grid(row=0,column=1)
        #ftame1pack()后才会显示

        tk.Label(frame2,text="密码").grid(row=2,column=0)
        tk.Entry(frame2,show="*",textvariable=self.password).grid(row=2,column=1)


        tk.Label(frame3,text="登陆方式").grid(row=0,column=0)
        self.selector = ttk.Combobox(frame3,values=("我是管理员","我不是管理员"),width="15")
        self.selector.grid(row=0,column=1)
        self.selector.current(0)
        self.selector.bind("<<ComboboxSelected>>", self.selector_listener)

        # self.selector["values"]= (1,2)

        frame3.grid(pady=15)
        frame1.grid(pady=15)
        frame2.grid(pady=15)

        #Button
        button=tk.Button(self,text="登录",width=15,command=self.Buttonclick)
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


