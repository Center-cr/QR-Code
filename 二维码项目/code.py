import cv2
import time
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk

##初始化摄像头对象
##s摄像头事件
global cap
cap = cv2.VideoCapture()
detector= cv2.QRCodeDetector()
##笔记本摄像头使用这个函数
# cap =cv2.VideoCapture(0)
def take_snapshot():
    print("有人给你点赞啦！")
def video_loop():
    global cap
    success,img = cap.read()
    if success:
        cv2.waitKey(1)
        cv2image = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)##转换颜色为RGBA
        current_image = Image.fromarray(cv2image)  # 把图像转换承Image对象
        imgtk = ImageTk.PhotoImage(image = current_image)
        root.config(cursor="arrow")
        panel = tk.Label(root)  ##图像通道
        panel.pack(padx=10, pady=10)
        # btn = tk.Button(root, text="点赞", command=take_snapshot)
        # btn.pack(fill="both", expand=True, padx=10, pady=10)
        panel.imgtk = imgtk
        panel.config(image=imgtk)
        root.after(1,video_loop)
    print("111")
    if success is False:
        # # 打印报错
        # print('read video error')
        # # 退出程序
        # exit(0)
        while success is False:##读取失败继续请求
            cap = cv2.VideoCapture('http://192.168.2.76:8080/shot.jpg')##无法注释
            success, img = cap.read()

    data, bbox, _ = detector.detectAndDecode(img)  ##识别二维码
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
            # 关键
            cv2.waitKey(1)  ##不让刷新太快避免卡死
            # img.save(filename)
            # cv2.waitKey(1)



filename = "qr_img.png"



if __name__ == '__main__':
    root = tk.Tk()
    root.title("opencv+tkinter")
    video_loop()
    root.mainloop()
    # 解码
    cap.release()
    cv2.destroyAllWindows()