# -*- coding: utf-8 -*-
"""
Created on Wed Nov 17 09:39:41 2021

@author: RezaKurniawan
"""
print("Program Menghitung jumlah range")
input1 = int(input("Angka 1: "))
input2 = int(input("Angka 2: "))

total = 0
for x in range(input1, input2+1, +1):
	total += x

print(f"Jumlah {total}")
