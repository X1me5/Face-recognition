# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 12:37:42 2020

@author: 王玺
"""
import pymssql

connect = pymssql.connect('(local)', 'sa', '', 'arrival')  #建立连接
if connect:
    print("连接成功!")
    
cursor = connect.cursor()   #创建一个游标对象,python里的sql语句都要通过cursor来执行
cursor.execute("create table arrival(id varchar(20))")   #执行sql语句
connect.commit()  #提交
cursor.close()   #关闭游标
connect.close()  #关闭连接