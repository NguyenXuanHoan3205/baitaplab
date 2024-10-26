# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 21:59:29 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

a=int(input("Nhập 1 số bất kì: "))
x= {0:"Khong",1:"Mot",2:"Hai",3:"Ba",4:"Bon",5:"Nam",6:"Sau",7:"Bay",8:"Tam",9:"Chin"}
if 0<=a<=9:
    print("Số vừa nhập là: ",x[a])
else:
    print("Khong doc duoc.")