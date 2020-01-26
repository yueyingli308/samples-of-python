# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 10:13:54 2020

@author: admin
"""

#Given an array of integers, find the first missing positive integer in linear time and constant space. 
def first_missing_positive(nums):
    s = set(nums)
    i = 1
    while i in s:
        i += 1
    return i

first_missing_positive([3, 4, -1, 1])

###相当于是从1开始挨个试这些数在不在列表里

##方法2
def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):  ##把list变成dic来进行编号
        while i + 1 != nums[i] and 0 < nums[i] <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1