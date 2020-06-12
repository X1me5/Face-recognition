# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:43:37 2020

@author: 王玺
"""

import cv2
import sys
 
from PIL import Image
 
def CatchPICFromVideo(window_name, camera_idx, catch_pic_num, path_name):
    cv2.namedWindow(window_name)
    cap = cv2.VideoCapture(camera_idx)                   
    #告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("C:\\Face recognition\\classifier\\haarcascade_frontalface_alt2.xml")
    color = (0, 255, 0)
    
    num = 0    
    while cap.isOpened():
        ok, frame = cap.read() 
        if not ok:            
            break                 
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #将当前桢图像转换成灰度图像                    
        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:          #大于0则检测到人脸                                   
            for faceRect in faceRects:  
                x, y, w, h = faceRect                                       
                #将当前帧保存为图片
                img_name = '%s/%d.jpg'%(path_name, num)                
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                cv2.imwrite(img_name, image)                                
                                
                num += 1                
                if num > (catch_pic_num):   #如果超过指定最大保存数量退出循环
                    break
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame,'num:%d' % (num),(x + 30, y + 30), font, 1, (255,0,255),4)                       
        #超过指定最大保存数量结束程序
        if num > (catch_pic_num): break                                      
        #显示图像
        cv2.imshow(window_name, frame)        
        c = cv2.waitKey(10)
        if c & 0xFF == ord('q'):
            break         
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    if len(sys.argv) != 1:
        print("Usage:%s camera_id face_num_max path_name\r\n" % (sys.argv[0]))
    else:
        CatchPICFromVideo("截取人脸", 0, 500, 'C:\\Face recognition\\data\\chengtianle')
