# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 21:20:50 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

a = int(input("Nhập số nguyên a: "))
b = int(input("Nhập số nguyên b: "))
c = int(input("Nhập số nguyên c: "))
d = int(input("Nhập số nguyên d: "))
smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c
if d < smallest:
    smallest = d
print(f"Số nhỏ nhất là: {smallest}")
