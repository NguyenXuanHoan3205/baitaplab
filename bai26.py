# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 23:30:49 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

#a
print ("a.")
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Thứ tự tăng dần: ", a, b, c)
#b
print("b.")
N = input("Nhập số nguyên: ")
dayso = "".join(sorted(N))
print("Dãy số theo thứ tự tăng dần: ", dayso)