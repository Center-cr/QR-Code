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
        self.vs = cv2.VideoCapture(0) #
        self.output_path = output_path  # 存储输出位置
        self.current_image = None  # current image from the camera

        self.root = tk.Tk()  # initialize root window
        self.root.title("PyImageSearch PhotoBooth")  # set window title
        # self.destructor function gets fired when the window is closed
        self.root.protocol('WM_DELETE_WINDOW', self.destructor)

        self.panel = tk.Label(self.root)  # initialize image panel
        self.panel.pack(padx=10, pady=10)

        # create a button, that when pressed, will take the current frame and save it to file
        btn = tk.Button(self.root, text="Snapshot!", command=self.take_snapshot)
        btn.pack(fill="both", expand=True, padx=10, pady=10)

        # start a self.video_loop that constantly pools the video sensor
        # for the most recently read frame
        self.video_loop()

    def video_loop(self):
        ok, frame = self.vs.read()  # read frame from video stream
        if ok:  # frame captured without any errors
            print("frame", type(frame))
            cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # 转换色值
            self.current_image = Image.fromarray(cv2image)  # 转为PIL可以处理的imge对象
            imgtk = ImageTk.PhotoImage(image=self.current_image)  # 转化为ikinter可以处理的图像
            # print(type(imgtk))
            self.panel.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
            self.panel.config(image=imgtk)  # tkinter显示图像
        else:
            while ok is False:##打开错误时
                self.vs.release()
                cv2.waitKey(1)
                self.vs = cv2.VideoCapture(0)
                ok, frame = self.vs.read()
                print("frame in False", type(frame))
                print("读取")
        self.root.after(30, self.video_loop)  # call the same function after 30 milliseconds
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

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-o","--output", default="./",
    help="path to output directory to store snapshots (default: current folder")
args = vars(ap.parse_args())

# start the app
print("[INFO] starting...")
pba = Application(args["output"])
pba.root.mainloop()