# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:21:23 2020

@author: admin
"""

#Given the root to a binary tree, implement serialize(root), 
#which serializes the tree into a string, and deserialize(s), 
#which deserializes the string back into the tree.


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def serialize(root):
    if root is None:
        return '#'
    return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))

def deserialize(data):
    def helper():
        val = next(vals)
        if val == '#':
            return None
        node = Node(int(val))
        node.left = helper()
        node.right = helper()
        return node
    vals = iter(data.split())
    return helper()