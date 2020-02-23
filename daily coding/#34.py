# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 15:13:37 2020

@author: admin
"""

##Given a string, find the palindrome that 
#can be made by inserting the fewest number of characters as possible anywhere in the word. 

##For example, given the string "race", you should return "ecarace"
##As another example, given the string "google", you should return "elgoogle".

def is_palindrome(s):
    return s == s[::-1]


def make_palindrome(s):
    if is_palindrome(s):
        return s
    if s[0] == s[-1]:
        return s[0] + make_palindrome(s[1:-1]) + s[-1]
    else:
        one = s[0] + make_palindrome(s[1:]) + s[0]
        two = s[-1] + make_palindrome(s[:-1]) + s[-1]
        if len(one) < len(two):
            return one
        elif len(one) > len(two):
            return two
        else:
            return min(one, two)
            
            
####思路：简单的recursive来进行
  

#######方法二： Dynamic Programming
cache = {}

def is_palindrome_2(s):
    return s == s[::-1]

def make_palindrome_2(s):
    if s in cache:
        return cache[s]

    if is_palindrome(s):
        cache[s] = s
        return s
    if s[0] == s[-1]:
        result = s[0] + make_palindrome(s[1:-1]) + s[-1]
        cache[s] = result
        return result
    else:
        one = s[0] + make_palindrome(s[1:]) + s[0]
        two = s[-1] + make_palindrome(s[:-1]) + s[-1]
        cache[s] = min(one, two)
        return min(one, two)
        