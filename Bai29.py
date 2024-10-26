# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 13:04:31 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai 29
n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))
s = 0 #Tong = 0
for i in range(1, n+1):
    s += n%10
    n//=10
print("Tong la: ", s)


    