import cv2
import time
##初始化摄像头对象


# cap =cv2.VideoCapture(0)
cap = cv2.VideoCapture('http://10.20.123.167:8080/shot.jpg')

detector= cv2.QRCodeDetector()

filename="qr_img.png"


# 如果解码成功77
while True:
    #捕获图像
    hx,img =cap.read()
    if hx is False:
        # # 打印报错
        # print('read video error')
        # # 退出程序
        # exit(0)
        while hx is False:
            cap = cv2.VideoCapture('http://10.20.123.167:8080/shot.jpg')
            hx, img = cap.read()
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
            print("point1", point1)
            print("point2", point2)
            print("point的类型为", type(point1))
            cv2.line(img, point1, point2, color=(255, 0, 0), thickness=2)
    # 打印图片
    if data:
        print(f"QRCode data:\n{data}")
    # 显示拍摄画面
    cv2.imshow("摄像头拍摄", img)
    #关键
    cv2.waitKey(1)
    img.save(filename)

cmp.relaase()
cv2.destroyAllWindows()