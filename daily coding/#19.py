# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 15:26:02 2020

@author: admin
"""

#Given an N by K matrix where the nth row and kth column represents the cost 
#to build the nth house with kth color, return the minimum cost which achieves this goal.

##Method1：using dynamic programming.

## We can maintain a matrix cache where every entry [i][j] represents 
#the minimum cost of painting house i the color j, as well as painting every house < i. 
#We can calculate this by looking at the minimum cost of painting each house < i - 1, 
#and painting house i - 1 any color except j, since that would break our constraint. 
#We'll initialize the first row with zeroes to start. 
#Then, we just have to look at the smallest value in the last row of our cache, 
#since that represents the minimum cost of painting every house.


def build_houses(matrix):
    n = len(matrix)
    k = len(matrix[0])   #第一行的list长度
    solution_matrix = [[0] * k]

    # Solution matrix: matrix[i][j] represents the minimum cost to build house i with color j.
    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)
        solution_matrix.append(row_cost)
    return min(solution_matrix[-1])

##简化的方法：

def build_houses_2(matrix):
    k = len(matrix[0])
    soln_row = [0] * k

    for r, row in enumerate(matrix):
        new_row = []
        for c, val in enumerate(row):
            new_row.append(min(soln_row[i] for i in range(k) if i != c) + val)
        soln_row = new_row
    return min(soln_row)

