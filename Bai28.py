# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:58:12 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai 28

n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))
for i in range(1, n+1):
    if n%i == 0:
        print("Uoc so cua N la: ", i)
        
        
