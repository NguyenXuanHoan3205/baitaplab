# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:30:31 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai45

ts = 1
ms = 0
s = 0
n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))
x = float(input("Nhap x: "))
#x^n = x**n = ts = 1
#1+2+3+...+n = ms = 0
for i in range(1,n+1):
    ts = x**i
    ms = ms + i
    s += ts/ms
print(round(s,2))

    
