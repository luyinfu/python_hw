#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 15:19:37 2020

@author: Luyin Fu
"""


'''
%cd /Users/tsuyu/Downloads/workspace
!git init
!git add "hw1.py"
!git commit -m "First commit"
!git remote add origin https://github.com/luyinfu/python_hw.git

!git push -u origin master
'''
# 1
## (a)
a=list(range(1,21))
print(a)
## (b)
list(range(20,0,-1))
## (c)
list(range(1,21))+list(range(20,0,-1))
## (d)
[4,6,3]*10
## (e)
a1=[4,6,3]*10
a1.append(4)
a1

# 2
import math
import numpy as np
l1=[]
for x in np.arange(3,6,0.1):
    l1.append(math.exp(x)*math.cos(x))
print(l1)


# 3
l2=[]
for i in range(1,26):
    k=2.0**i/i
    l2.append(k)
print(l2)
    


# 4
## (a)
l3=[]
n=10
b=a[0:n]
for i in range(len(b)):
    l3.append(b[i]-b[-(i+1)])
print(l3)

## (b)
l4=[]
for i in range(len(a)):
    l4.append(a[i]%2==0)
print(l4)


# 5
## (a)
import re
with open('lorem.txt', 'r') as file:
    f = file.read().replace('\n', '') #open the file and save it as a string

## (b)
result = re.match('([A-Z]+)', f)
print(result)
#pat = re.compile('([A-Z][a-z]+)|\W([a-z]{5})\W')













    




