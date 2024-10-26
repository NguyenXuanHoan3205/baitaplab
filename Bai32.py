# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:34:39 2024

@author: Nguyen Xuan Hoan - 23694771
"""
#Bai32

km = float(input("Nhap vao so km: "))
tien = 0

if km <=1 and km > 0:
    tien = 15000
    print("So tien: ", tien)
elif 1<km<6:
    tien = 15000 + (km-1)*13500
    print("So tien: ", tien)
elif km >= 6:
    tien = 15000 + 4*13500 + (km-5)*11000
    print("So tien la: ", tien)
else:
    print("Khong hop le")
if km > 120:
    tien = (15000 + 4*13500 + (km-5)*11000)*0.9
    print("So tien la: ", tien)

    
    
    