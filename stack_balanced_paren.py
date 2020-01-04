# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 10:11:04 2020

@author: User
"""
from Stack import stack


def is_match(p1,p2):
    if p1=="{" and p2=="}":
        return True
    elif p1=="(" and p2==")":
        return True
    elif p1=="[" and p2=="]":
        return True
    else: 
        return False
    
def check_paren_bal(string_paren):
     s=stack()
     is_bal=True
     index=0
     print(len(string_paren))
     #print()
     
     while index< len(string_paren) and is_bal:
         paren=string_paren[index]
         print(paren)

         if paren in "{[(":
             s.push(paren)
             
         else:
             if s.is_empty():
                 is_bal=False
                 
             else:
                 top=s.pop()
                 if not is_match(top,paren):
                     is_bal=False
         print(s.getstack())
         index+=1
                     
     if s.is_empty() and is_bal:
         return True
     else:
         return False
    
print(check_paren_bal("{[]}"))
    
    

     