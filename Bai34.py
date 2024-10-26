# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:23:05 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai34

n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))
if n < 2:
    print("Khong phai so nguyen to")
else:
    for i in range(2,n+1):
        if n%i==0:
            print("Khong phai so nguyen to")
            break
        else:
            print("la so nguyen to")
            break
        
        
        