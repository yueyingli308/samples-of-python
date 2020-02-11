# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:09:21 2020

@author: admin
"""

#Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), 
#find the minimum number of rooms required.

#For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

def max_overlapping(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)  #注意处理方法是‘sorted+简短for循环
    print(starts,ends)

    current_max = 0
    current_overlap = 0
    i, j = 0, 0
    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            current_overlap += 1
            current_max = max(current_max, current_overlap)
            i += 1
        else:
            current_overlap -= 1
            j += 1   #这里非常重要！
            #任意一个不overlap的时间段，其开始时间必会start>上一个end,之后必会小于一个end(起码是自己时间段括号的)
            #所以上面+1 这里减1 持平！
        print(current_overlap)
    return current_max


max_overlapping([(30, 75), (0, 50), (60, 150),(70,140)])            