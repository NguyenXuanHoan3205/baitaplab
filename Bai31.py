# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:20:52 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai 31

a = int(input("Nhap vao canh a: "))
b = int(input("Nhap vao canh b: "))
c = int(input("Nhap vao canh c: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Day la tam giac deu.")
    elif a == b or b == c or a == c:
        print("Day la tam giac can.")
    elif a**2 + b**2 == c**2:
        print("Day la tam giac vuong.")
    else:
        print("Day la tam giac thuong.")
else:
    print("a,b,c khong phai la canh cua tam giac.")
    
    