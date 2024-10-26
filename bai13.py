# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 18:55:04 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

day = int(input("Nhập ngày: "))
month = int(input("Nhập tháng: "))
year = int(input("Nhập năm: "))
d = year%100
print("a> Ngày/tháng/năm: ",f"{day}/{month}/{year}")
print("b> Ngày/tháng/năm: ",f"{day}/{month}/{d}")
print("c> Năm/tháng/ngày: ",f"{year}/{month}/{day}")
    