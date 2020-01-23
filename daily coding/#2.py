# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 15:20:54 2020

@author: admin
"""

#Given an array of integers, return a new array such that each element at index i of the new array is the 
#product of all the numbers in the original array except the one at i.

#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
#If our input was [3, 2, 1], the expected output would be [2, 3, 6].

#Sol 1
def products(nums):
    prefix_products = []
    for num in nums:
        if prefix_products:
            prefix_products.append(prefix_products[-1] * num)
        else:
            prefix_products.append(num)
            ##每个数连续和前面的数相乘
            #输入 [1, 2, 3, 4, 5] 输出 [1, 2, 6, 24, 120]
            
    suffix_products = []
    for num in reversed(nums):
        if suffix_products:
            suffix_products.append(suffix_products[-1] * num)
        else:
            suffix_products.append(num)
    suffix_products = list(reversed(suffix_products))
#输入 [1, 2, 3, 4, 5] 输出 [120, 120, 60, 20, 5]

    # Generate result
    result = []
    for i in range(len(nums)):
        if i == 0:
            result.append(suffix_products[i + 1])
        elif i == len(nums) - 1:
            result.append(prefix_products[i - 1])
        else:
            result.append(prefix_products[i - 1] * suffix_products[i + 1])
    return result
products([1, 2, 3, 4, 5])
