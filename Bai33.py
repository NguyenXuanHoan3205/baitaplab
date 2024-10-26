# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:13:56 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai33
import math
n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))
    
can_2 = math.sqrt(n)
if n == int(can_2**2):
    print("So chinh phuong.")
else:
    print("Khong phai la so chinh phuong.")
