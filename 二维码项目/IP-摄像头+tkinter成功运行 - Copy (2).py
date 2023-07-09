from PIL import Image, ImageTk
import tkinter as tk
import argparse
import datetime
import cv2
import os
global PATH
PATH = 'http://192.168.2.76:8080/shot.jpg'
class Application:
    def __init__(self, output_path ="./"):
        self.vs = cv2.VideoCapture(PATH) #
        self.output_path = output_path  # 存储输出位置
        self.current_image = None  # current image from the camera

        self.root = tk.Tk()  # 初始化屏幕
        self.root.title("QR code")  # 窗口名字
        # 销毁协议，窗口关闭时销毁程序
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)  # 初始化图像面板
        self.panel.pack(padx=10, pady=10)

        # 创建按钮，当点击保存的时候会保存到相应路径
        self.btn = tk.Button(self.root, text=".!.拍照.!.", command=self.take_snapshot)
        self.btn.pack(fill="both", expand=True, padx=10, pady=10)
        self.btn.grid_propagate(0)
        ##开始不断提取画面
        self.video_loop()


    def video_loop(self):
        ok, frame = self.vs.read()  # 读取帧
        if ok:  # 读取到图像时
            print("frame", type(frame))
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 转换色值
            self.current_image = Image.fromarray(cv2image)  # 转为PIL可以处理的imge对象
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # 转化为ikinter可以处理的图像
            # print(type(imgtk))
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)  # tkinter显示图像
        else:
            while ok is False:##打开错误时
                # self.vs.release()
                cv2.waitKey(1)
                self.vs = cv2.VideoCapture(PATH)
                ok, frame = self.vs.read()
                print("frame in False", type(frame))
                print("读取")
        ##关键代码，在跳出wrong循环后快速显示图像，避免图像
        print("函数最后。。。。。。frame", type(frame))
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 转换色值
        self.current_image = Image.fromarray(cv2image)  # 转为PIL可以处理的imge对象
        imgtk = ImageTk.PhotoImage(image=self.current_image)  # 转化为ikinter可以处理的图像
        # print(type(imgtk))
        self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        self.panel.config(image=imgtk)  # tkinter显示图像
        ##重新建立
        self.btn.pack()
        print(".......显示成功........")
        self.root.after(1,self.video_loop)
        # btn = tk.Button(self.root, text=".!.拍照.!.", command=self.take_snapshot)
        # btn.pack(fill="both", expand=True, padx=10, pady=10)

    def take_snapshot(self):
        ts = datetime.datetime.now() # grab the current timestamp
        filename ="{}.jpg".format(ts.strftime("%Y-%m-%d_%H-%M-%S"))  # construct filename
        p = os.path.join(self.output_path, filename)  # construct output path
        self.current_image.save(p,"JPEG")  # save image as jpeg file
        print("[INFO] saved {}".format(filename))

    def destructor(self):
        print("[INFO] closing...")
        self.root.destroy()
        self.vs.release()  # release web camera
        cv2.destroyAllWindows()  # it is not mandatory in this application

# # construct the argument parse and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-o","--output", default="./",
#     help="path to output directory to store snapshots (default: current folder")
# args = vars(ap.parse_args())

# start the app
print("[INFO] starting...")
pba = Application()
pba.root.mainloop()
