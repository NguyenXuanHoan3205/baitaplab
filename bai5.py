# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 15:46:52 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

h=int(input("Nhập giờ: "))
m=int(input("Nhập phút: "))
s=int(input("Nhập giây: "))
print("Thời gian đã nhập: ",f"{h}:{m}:{s}")
print("Thời gian theo giây: ", h*3600+m*60+s,"(s)")
