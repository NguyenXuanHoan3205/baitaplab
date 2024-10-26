# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 21:55:30 2024

@author: Asus
"""

n = int(input("Enter n: "))

while n < 0:
    print("Please enter a non-negative number.")
    n = int(input("Enter n: "))

print("Ước số của", n, "là", end=" ")
for i in range(1, n+1):
    if n % i == 0:
        print(i, end=" ")