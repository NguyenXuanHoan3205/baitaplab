# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 23:19:35 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

a = input("Hãy nhập một chữ cái: ")
if a.islower():
    print("Ký tự chữ hoa:", a.upper())
else:
    print("Ký tự chữ thường:", a.lower())