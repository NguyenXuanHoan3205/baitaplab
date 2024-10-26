# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 21:40:13 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

a=int(input("Số nguyên a: "))
b=int(input("Số nguyên b: "))
c=int(input("Số nguyên c: "))
if a>c and a>b:
    print("Số có giá trị lớn nhất là:",a)
elif b>a and b>c:
    print("Số có giá trị lớn nhất là:",b)        
else:
    print("Số có giá trị lớn nhất là:",c)