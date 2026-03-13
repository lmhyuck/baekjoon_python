# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 11:04:49 2026

@author: human
"""
import sys

sum=0
for argv in sys.argv[1:]:
    sum+= int(argv)
print(sum)