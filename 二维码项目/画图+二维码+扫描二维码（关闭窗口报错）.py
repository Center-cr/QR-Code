import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import matplotlib
import matplotlib.pyplot as plt
import numpy
import numpy as np
import cv2
import qrcode
from PIL import Image # 导入PIL库
import os


detector= cv2.QRCodeDetector()



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
        self.filename = "img.jpg"

        #二维码扫描
        self.cap = cv2.VideoCapture(0)


        self.pack()
        self.envar= tk.StringVar(None,"123")
        root.geometry('550x270')
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

        if self.select.get() == "二维码生成":
            print("二维码")
            data = self.str_para.get()
            if len(data)== 0:
                messagebox.showinfo("提示", " 请输入正确信息")
                return
            img = qrcode.make(data)
            img.save(self.filename)
            print("成功生成二维码")
            return

    def Button1click(self):
        if self.select.get() == "二维码生成":
            if os.path.exists('./img.jpg') is False:
                messagebox.showinfo("提示", " 还未生成图片")
                return
            img = Image.open('./img.jpg')
            img.show()
        else:
            messagebox.showinfo("提示", " 模式选择错误")

    def Button2click(self):
        if self.select.get() == "扫描二维码":
            self.video_loop()
        else:
            messagebox.showinfo("提示", " 模式选择错误")

    def video_loop(self):
        while self.select.get() == "扫描二维码":
            # 捕获图像

            hx, img = self.cap.read()
            print("进入二维码扫描")
            if hx is False:
                while (hx is False) and (self.select.get() == "二维码生成"):
                    print("连接照相机")
                    self.cap = cv2.VideoCapture(0)
                    hx, img = self.cap.read()
                    cv2.waitKey(1)
            # 解码
            data, bbox, _ = detector.detectAndDecode(img)
            if bbox is not None:
                # 用线条显示图像
                # 边框长度
                print("bbox", bbox)
                print("bbox是一个", type(bbox))
                n_lines = int(bbox.size / 2)
                print("n_lines", n_lines)
                for i in range(n_lines):
                    point1 = tuple(bbox[0][i])
                    point1 = (int(point1[0]), int(point1[1]))
                    point2 = tuple(bbox[0][(i + 1) % n_lines])
                    point2 = (int(point2[0]), int(point2[1]))
                    cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
            # 打印图片
            if data:
                print(f"QRCode data:\n{data}")
            # 显示拍摄画面
            cv2.imshow("摄像头拍摄", img)
            if cv2.waitKey(1) == ord('q'):
                # self.cap.release()
                # cv2.destroyAllWindows()
                break
            # 点击窗口关闭按钮退出程序
            if cv2.getWindowProperty("摄像头拍摄", cv2.WND_PROP_AUTOSIZE) < 1:
                # self.cap.release()
                cv2.destroyAllWindows()
            # 点击小写字母q 退出程序
                break
            # cv2.waitKey(1)
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
        self.selector = ttk.Combobox(frame1,values=("一元函数","二元函数","二维码生成","扫描二维码"),width="15")
        self.selector.grid(row=0,column=1)
        self.selector.current(0)
        self.selector.bind("<<ComboboxSelected>>", self.selector_listener)

        # self.selector["values"]= (1,2)

        # frame3.grid(pady=15)

        # frame2.grid(pady=15)

        #Button
        button=tk.Button(frame2,text="运行图像",width=15,command=self.Buttonclick)
        button.grid(row=0,column=1,padx=5)
        button1=tk.Button(frame1,text="打开二维码",width=10,command=self.Button1click)
        button1.grid(row=3,column=3,padx=1)

        button2=tk.Button(frame1,text="扫描二维码",width=10,command=self.Button2click)
        button2.grid(row=3,column=5,padx=1)

        frame1.grid(pady=15)
        frame2.grid(pady=15)
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


