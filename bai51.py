# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:42:14 2024

@author: honan
"""

#Bài tập LAB1:
#Bài 51:

def ktra_gtri():
    n = input("Nhập vào n: ")
    if n.replace(',','',1).replace('-','',1).isdigit():
        n = float(n)
    if -89 <= n <= 90:
        return n 
    print("Không hợp lệ, nhập ")
    return ktra_gtri()
print(ktra_gtri())
