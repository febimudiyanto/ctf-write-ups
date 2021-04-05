'''
Python Decode Ascii

author : Febi Mudiyanto
date   : 5-04-2021


'''
import os
from os import path

file_ = input("masukkan nama file = ")
with open(file_) as f:
    line = f.readlines()
    for i in range(len(line)):
        num = line[i][:-2]
        print(chr(int(num)),end="")
