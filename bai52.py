# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 12:56:55 2024

@author: Nguyen Xuan Hoan 
"""

#Bai52
import math
#a
def canbac(x,n):
    return x**(1/n)
#b
def sodao(n):
    #str: chuỗi, chữ số
    #return str(n)[::-1]
    return int(str(n)[::-1])
#cách 3
def dao(n):
    dao=0
    while n>0:
        dao=dao*10+n%10
        n//10
    return dao
#c
def chinhphuong(n):
    return int(math.sqrt(n))**2 == n
#d
def ktra_ngto(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
    return True
#e
def tich_sole(n):
    tich = 1
    for i in str(n):
        if int(i)%2 != 0:
            tich *= int(i)
    return tich
#f
def tong_ngto(n):
    tong_ngto = 0 
    for i in range(2,n):
        if ktra_ngto(i):
            tong_ngto += i
    return tong_ngto
#g
def tong_cp(n):
    tong = 0 
    for i in range(1,n):
        if chinhphuong(i):
            tong += i
    return tong
#h
def tong_uoc(n):
    tong = 0
    for i in range(1,n+1):
        if n%i == 0:
            tong += i
    return tong
if __name__ =="__main__":
    print(canbac(8,3))
    print(sodao(123450))
    print(chinhphuong(1))
    print(ktra_ngto(2))
    print(tich_sole(135))
    print(tong_ngto(20))
    print(tong_cp(9))
    print(tong_uoc(8))
    
    
    
  
