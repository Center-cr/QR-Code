import cv2
import time
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
##初始化摄像头对象
global PATH
PATH = 'http://192.168.2.76:8080/shot.jpg'

# cap =cv2.VideoCapture(0)
global cap
cap = cv2.VideoCapture(PATH)

detector= cv2.QRCodeDetector()

filename="qr_img.png"
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
def video_loop():
# 如果解码成功77
    #捕获图像
    global PATH
    global cap
    print("11111")
    hx,img =cap.read()
    if hx is False:
        # # 打印报错
        # print('read video error')
        # # 退出程序
        # exit(0)
        while hx is False:
            cv2.waitKey(10)
            print("waiting............")
            cap = cv2.VideoCapture(PATH)
            hx, img = cap.read()

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
            print("point1", point1)
            print("point2", point2)
            print("point的类型为", type(point1))
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
    # 打印图片
    if data:
        print(f"QRCode data:\n{data}")
    # 显示拍摄画面
    cv2.imshow("摄像头拍摄", img)
    application.after(1,video_loop)



root = tk.Tk()
application = Application(root=root)
video_loop()
application.mainloop()#创建tk对象
    # cmp.relaase()
    # cv2.destroyAllWindows()
    # #关键
    # cv2.waitKey(1)
#'httpp://10.20.123.167:8080/shot.jpg'
