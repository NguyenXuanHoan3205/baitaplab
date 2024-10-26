# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 23:40:09 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

import math
print("Hãy chọn hình theo tắc: hình vuông(v), hcn(n), hình tròn(t)")
a = input("nhập hình theo quy tắc trên: ")
if a == "v":
    b = int(input("Nhập cạnh hình vuông: "))
    C = b*4
    S = b*b
    print("Chu vi hình vuông: ", C)
    print("Diện tích hình vuông: ", S)
elif a == "n":
    b = int(input("Nhập chiều dài: "))
    c = int(input("Nhập chiều rộng: "))
    C = (b + c)*2
    S = b * c
    print("Chu vi hcn: ", C)
    print("Diện tích hcn: ", S)
elif a == "t":
    b = int(input("Nhập bán kính: "))
    C = (b*2) * math.pi
    S = (b**2) * math.pi
    print("Chu vi hình tròn: ", C, "Diện tích hình tròn: ", S)