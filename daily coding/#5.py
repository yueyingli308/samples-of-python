# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:43:49 2020

@author: admin
"""


#cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. 
#For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
    return pair(lambda a, b: a)

def cdr(pair):
    return pair(lambda a, b: b)

cdr(cons(3, 4))
#return result is 4