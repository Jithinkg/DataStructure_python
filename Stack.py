# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 09:47:19 2020

@author: User
"""

class stack:
    def __init__(self):
        self.items=[]
    def push(self,a):
        self.items.append(a)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items==[]
    def peek(self):
        if not self.isempty():
            return self.items[-1]
    def getstack(self):
        return self.items
        
#s=stack()
#s.push("B")
#print(s.isempty())
#print(s.peek())