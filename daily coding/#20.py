# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 21:52:15 2020

@author: admin
"""

###Given two singly linked lists that intersect at some point, find the intersecting node. 
#The lists are non-cyclical.

#For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.


def length(head):
    if not head:
        return 0
    return 1 + length(head.next)

def intersection(a, b):
    m, n = length(a), length(b)
    cur_a, cur_b = a, b

    if m > n:
        for _ in range(m - n):   #这里不太确定为什么要把长的list向后越过多处的长度一部分
            cur_a = cur_a.next
    else:
        for _ in range(n - m):
            cur_b = cur_b.next

    while cur_a != cur_b:
        cur_a = cur_a.next
        cur_b = cur_b.next
    return cur_a

