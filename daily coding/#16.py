# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 13:34:52 2020

@author: admin
"""

##EASY

###You run an e-commerce website and want to record the last N order ids in a log. 
##Implement a data structure to accomplish this, with the following API

class Log(object):
    def __init__(self, n):
        self._log = []
        self.n = n

    def record(self, order_id):
        if len(self._log) >= self.n:
            self._log.pop(0)
        self._log.append(order_id)

    def get_last(self, i):
        return self._log[-i]
    
    