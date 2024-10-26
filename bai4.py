# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 15:21:34 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

n = int(input("Nhập vào số nguyên n: "))
a = n // 10
b = n % 10
if n > 9 and n < 100:
    print("Tổng các chữ số của {n} là: ", a+b)   
else:
    print ("Số bạn vừa nhập không hợp lệ")
    