# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 16:09:42 2020

@author: admin
"""

##Dynamic Programming

#1.1 Package Problem
#背包问题

#Description
#首先我们先构建一个表格dp[i][j]，横轴为背包的容纳重量（从1到背包的实际最大容纳），纵轴为各个可选择的物品。
#而表格中的每个单元格表示的是使用i与前的物品、且保证总重量不大于j情况下背包能容纳物品的最大价值。

#Line of thinking
#在i行j列的最大值可以说是（i-1行[即不取i物品]j列的值) 和 (i物品的价值 + i-1行j-i物品价值列的值[即取了i物品的价值])，
#写成状态转移方程即为：`dp[i][j] = max{dp[i-1][j], dp[i-1][j-value[i]] + value[i]}，对应的代码如下：


#Codes:
# n个物体的重量(w[0]无用)
weight = [1, 4, 3, 1]
# n个物体的价值(p[0]无用)
value = [1500, 3000, 2000, 2000]
# 计算n的个数
n = len(weight) - 1
# 背包的载重量
capacity = 5
# 装入背包的物体的索引
x = []

def bag_dynamic(weight, value, capacity, x):
    n = len(weight)
    weight.insert(0, 0)
    value.insert(0, 0)

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if j >= weight[i]:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i]] + value[i])
            else:
                dp[i][j] = dp[i - 1][j]
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            x.append(i)
            j = j - weight[i]

    return dp[n][capacity]