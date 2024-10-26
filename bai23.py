# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 22:35:03 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

# Nhập các hệ số 
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
delta = b**2 - 4*a*c
print ("Giải phương trình bậc 2: ax^2 + bx + c = 0")
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x =", -b/(2*a))
else:
    print("Phương trình có hai nghiệm phân biệt", (-b + delta**0.5)/(2*a), "và", (-b + delta**0.5)/(2*a))