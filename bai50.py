# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 14:39:54 2024

@author: honan
"""

#Bài tập LAB1:
#Bài 50:
    
def ktra_gtri(n):
    if n < 0 and n%2 != 0:
        return -1
    elif n > 0 and n%2 == 0:
        return 1
    return 0
print(ktra_gtri(2))
