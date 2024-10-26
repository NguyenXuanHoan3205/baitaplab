# -*- coding: utf-8 -*-
"""
Created on Mon Sep 2 22:50:19 2024

@author: Nguyễn Xuân Hoan - 23694771
"""

h = int(input("Nhập giờ: "))
m = int(input("Nhập phút: "))
s = int(input("Nhập giây: "))
if h > 24 and m > 60 and s > 60:
    print ("Giờ, phút, giây không hợp lệ")
elif h > 24 and m > 60:
    print ("Giờ, phút không hợp lệ")
elif  h > 24 and s > 60:
    print ("Giờ, giây không hợp lệ")
elif m > 60 and s > 60:
    print ("Phút, giây không hợp lệ")
elif h > 24:
    print ("Giờ không hợp lệ")
elif m > 60:
    print ("Phút không hợp lệ")
elif s > 60:
    print ("Giây không hợp lệ")

else:
    print (h,":",m,":",s)