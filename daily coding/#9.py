# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 23:11:10 2020

@author: admin
"""

##Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. 
#Numbers can be 0 or negative.

##For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. 

def largest_non_adjacent(arr):
    if not arr:
        return 0

    return max(
            largest_non_adjacent(arr[1:]),
            arr[0] + largest_non_adjacent(arr[2:]))
    
### recursive的办法来解决
#### Time Compl = O(2^n)
    


##另一个个方法：
#Time Complexity = O(n)    
def largest_non_adjacent_2(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for i in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])  ##采取循环的方式来对比相加
    return cache[-1]
