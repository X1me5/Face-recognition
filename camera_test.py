# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 21:10:49 2020

@author: 王玺
"""

import cv2
from  train_model import Model
from  read_data import read_name_list

class Camera_reader(object):
    
    #在初始化camera的时候建立模型，并加载已经训练好的模型
    def __init__(self):
        self.model = Model()
        self.model.load()
        self.img_size = 128


    def build_camera(self):
        
        #opencv文件中人脸级联文件的位置，用于帮助识别图像或者视频流中的人脸
        face_cascade = cv2.CascadeClassifier('C:\\Face recognition\\classifier\\haarcascade_frontalface_alt2.xml')
        #读取dataset数据集下的子文件夹名称
        name_list = read_name_list('C:\\Face recognition\\data')

        #打开摄像头并开始读取画面
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()   #读取一帧视频
        while ret and cv2.waitKey(10)==-1:
            ret, frame = cap.read()
            try:
             gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #图像灰化
             faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))#识别人脸,******

             for (x, y, w, h) in faces:
                ROI = gray[y - 10: y + h + 10, x - 10: x + w + 10]
                ROI = cv2.resize(ROI, (self.img_size, self.img_size), interpolation=cv2.INTER_LINEAR)
                label,prob = self.model.predict(ROI)  #利用模型对cv2识别出的人脸进行比对
                if prob >0.90:    #如果模型认为概率高于95%则显示为模型中已有的label
                    show_name = name_list[label]
                else:
                    show_name = 'Stranger'
                cv2.putText(frame, show_name, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 1, 255, 2)  #显示名字
                frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  #在人脸区域画一个正方形
             cv2.imshow("Camera", frame)          
            except:continue
        cap.release()
        cv2.destroyAllWindows()
        return show_name
if __name__ == '__main__':
    camera = Camera_reader()
    camera.build_camera()