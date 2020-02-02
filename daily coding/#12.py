# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:56:15 2020

@author: admin
"""

###staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, 
##write a function that returns the number of unique ways you can climb the staircase.


##Use recursive func.

def staircase(n):
    if n==1:
        return 1
    if n == 0:
        return 1  ###注意这里也要设置为1，可以把2带入去看
    return staircase(n-1)+staircase(n-2)