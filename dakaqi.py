# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 18:05:44 2020

@author: 王玺
"""

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
import os
import numpy as np
import pymssql
import datetime
import time
from train_model import Model
from dataSet import DataSet
from camera_test import Camera_reader
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
from PyQt5.QtWidgets import QApplication, QMainWindow
#导入designer工具生成的login模块
from program import Ui_Form
from load_data import CatchPICFromVideo
class MyMainForm(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.ConfirmButton1.clicked.connect(self.setsavepath)
        self.RecordButton.clicked.connect(self.record)
        self.TrainButton.clicked.connect(self.train)
        self.BeginButton.clicked.connect(self.begin)
        self.addButton.clicked.connect(self.add)
        self.searchButton.clicked.connect(self.search)
        self.changeButton.clicked.connect(self.change)
        self.deleteButton.clicked.connect(self.delete)
        self.refreshButton.clicked.connect(self.refresh)
        self.checkButton.clicked.connect(self.check)
        self.picsave.setText("C:\Face recognition\data")
    def setsavepath(self):
        pathroad=self.picsave.text()
        os.mkdir(pathroad)
    def record(self):
        pathroad=self.picsave.text()
        CatchPICFromVideo("截取人脸", 0, 500, pathroad)           
    def train(self):
        dataset = DataSet('./data/')
        model = Model()
        model.read_trainData(dataset)
        model.build_model()
        model.train_model()
        model.evaluate_model()
        model.save()
    def begin(self):
        camera = Camera_reader()  
        show_name=camera.build_camera()
        if show_name == "Stranger":
            print("非本公司员工")
        else:
                 now_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
                 connect = pymssql.connect('(local)', 'sa', '', 'arrival') 
                 cursor = connect.cursor()
                 sql="update arrival set status='arrived',time='%s' where name='%s'"%(now_time,show_name)
                 cursor.execute(sql)           
                 connect.commit()  #提交
                 print("打卡成功！")
                 sql="select id,name,status,time from arrival where name='%s'"%(show_name)
                 cursor.execute(sql)
                 result=cursor.fetchall()
                 connect.commit()  #提交
                 print (result)            
                 cursor.close()   
                 connect.close()
    def add(self):
        name=self.picname.text()
        number=self.picnumber.text()
        connect = pymssql.connect('(local)', 'sa', '', 'arrival')  #建立连接
        if connect:
             print("新增成功!")  
        cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
        sql = "insert into arrival(id,name,time,status) values('%s','%s','No time','absent')"%(number,name)
        cursor.execute(sql)   #执行sql语句
        connect.commit()  #提交
        cursor.close()   
        connect.close() 
    def check(self):
        connect = pymssql.connect('(local)', 'sa', '', 'arrival')  #建立连接
        if connect:
             print("检测成功!") 
        cursor = connect.cursor()
        sql="select id,name,status,time from arrival where status='absent'"
        cursor.execute(sql)
        result=cursor.fetchall()
        connect.commit()  #提交
        print (result)
        cursor.close()   
        connect.close() 
    def search(self):
        connect = pymssql.connect('(local)', 'sa', '', 'arrival')  #建立连接
        if connect:
             print("查询成功!") 
        cursor = connect.cursor()
        number=self.picnumber.text()
        sql="select id,name,status,time from arrival where id='%s'"%(number)
        cursor.execute(sql)
        result=cursor.fetchall()
        connect.commit()  #提交
        print (result)
        cursor.close()   
        connect.close() 
    def change(self) :
        name=self.picname.text()
        number=self.picnumber.text()
        connect = pymssql.connect('(local)', 'sa', '', 'arrival')  #建立连接
        if connect:
             print("更新成功!")  
        cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
        sql = "update arrival set name='%s' where id='%s'"%(name,number)
        cursor.execute(sql)   #执行sql语句
        connect.commit()  #提交
        cursor.close()   
        connect.close() 
    def delete(self):
        number=self.picnumber.text()
        connect = pymssql.connect('(local)', 'sa', '', 'arrival')  #建立连接
        if connect:
             print("删除成功!")  
        cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
        sql = "delete from arrival where id='%s'"%(number)
        cursor.execute(sql)   #执行sql语句
        connect.commit()  #提交
        cursor.close()   
        connect.close() 
    def refresh(self):
        connect = pymssql.connect('(local)', 'sa', '', 'arrival') 
        cursor = connect.cursor()
        sql = "update arrival set status='absent',time='No time'"
        cursor.execute(sql)   #执行sql语句
        connect.commit()  #提交
        cursor.close()   
        connect.close() 
    #初始化
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.setWindowTitle(("打卡器"))
    myWin.setFixedSize(600,600)
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())