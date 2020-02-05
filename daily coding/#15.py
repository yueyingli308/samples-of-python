# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 13:44:32 2020

@author: admin
"""

##Given a stream of elements too large to store in memory, 
##pick a random element from the stream with uniform probability


###思路：
##For i >= 0, before the loop began, any element K in [0, i - 1] 
#had 1 / i chance of being chosen as the random element. 
#We want K to have 1 / (i + 1) chance of being chosen after the iteration. 
#This is the case since the chance of having being chosen already but not getting swapped with the ith element is 
#1 / i (1 - (1 / (i + 1))) which is 1 / i i / (i + 1) or 1 / (i + 1)
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if random.randint(1, i + 1) == 1:   ##这个方法产生离散均匀分布的整数，这些整数大于等于low，小于high
            ##相当于建立了一个1/(i)的概率
            random_element = e
    return random_element

###Summary：
##method：蓄水池采样(Reservoir Sampling)算法
##先选取数据流中的前k个元素，保存在集合A中；
#从第j（k + 1 <= j <= n）个元素开始，每次先以概率p = k/j选择是否让第j个元素留下。若j被选中，则从A中随机选择一个元素并用该元素j替换它；否则直接淘汰该元素；
#重复步骤2直到结束，最后集合A中剩下的就是保证随机抽取的k个元素。

