# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:12:41 2020

@author: admin
"""

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Easy part

#Sol 1
def two_sum_1(lst, k):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] + lst[j] == k:
                return True
    return False
  
#Sol 2
def two_sum_2(lst, k):
    seen = set()
    for num in lst:
        if k - num in seen:
            return True
        seen.add(num)  
    return False