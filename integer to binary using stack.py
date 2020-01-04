# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 12:39:24 2020

@author: User
"""

from Stack import stack

def div_by_2(dec):
    s=stack()
      
    
    while dec>0:
        r=dec%2
        s.push(r)
        dec=dec//2
    bin=""

    while  not s.is_empty():
        bin+=str(s.pop())
    return bin
    
print(div_by_2(242))
print(int(11110010,2))
        
