# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 17:30:34 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai 40

s = 0
n = int(input("Nhap N: "))
while n <= 0:
    n = int(input("Nhap lai N: "))
    
for i in range(1,n+1):
    s += 1/2*i
print(round(s,2))

