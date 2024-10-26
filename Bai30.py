# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:05:49 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai 30
thang = int(input("Nhap thang (1-12): "))
nam = int(input("Nhap nam: "))

if 1 <= thang <= 12:
    if thang in {1,3,5,7,8,10,12}:
        ngay = 31
    elif thang == 2:
        if(nam%4 == 0 and nam %100 != 0) or nam %400 == 0:
            ngay = 29
            print("Nam nhuan.")
        else:
            ngay = 28
            print("Khong phai nam nhuan.")
    else:
        ngay = 30
print(f"Thang {thang} nam {nam} co {ngay} ngay.")

