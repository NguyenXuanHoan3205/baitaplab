# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 19:58:32 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

a = int(input("Nhập giờ: "))
b = int(input("Nhập phút: "))
c = int(input("Nhập giây: "))
d = a*3600+b*60+c
print("Thời gian",f"{a}h{b}p{c}s","=",d,"giây")
