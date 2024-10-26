# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:54:50 2024

@author: honan
"""

#bai53
#a
def tong_1(n):
    s = 0
    for i in range(1,n+1):
        s += i
    return s
#b
def tong_2(n):
    s = 0
    for i in range(1,n+1):
        s += i**2
    return s
#c
def tong_3(n):
    s = 0
    for i in range(1,n+1):
        s += 1/i
    return s
#d
def tong_4(n):
    s = 0
    giaithua = 1
    for i in range(1,n+1):
        giaithua += i
        s += giaithua
    return s
#e
def tong_5(n):
    giaithua = 1
    for i in range(1,n+1):
        giaithua *= i
    return giaithua
print(tong_1(2))
print(tong_2(2))
print(tong_3(2))
print(tong_4(2))
print(tong_5(2))
