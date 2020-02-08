# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:51:38 2020

@author: admin
"""

##Given a string representing the file system in the above format, 
#return the length of the longest absolute path to a file in the abstracted file system. 
#If there is no file in the system, return 0.


#Step1
# first parse the string representing the file system and then get the longest absolute path to a file.

def build_fs(input):
    fs = {}
    files = input.split('\n')

    current_path = []
    for f in files:
        indentation = 0
        while '\t' in f[:2]:
            indentation += 1
            f = f[1:]

        current_node = fs
        for subdir in current_path[:indentation]:
            current_node = current_node[subdir]

        if '.' in f:
            current_node[f] = True
        else:
            current_node[f] = {}

        current_path = current_path[:indentation]
        current_path.append(f)

    return fs


#step2
#Computing the longest path

def longest_path(root):
    paths = []
    for key, node in root.items():
        if node == True:
            paths.append(key)
        else:
            paths.append(key + '/' + longest_path(node))
    # filter out unfinished paths
    paths = [path for path in paths if '.' in path]
    if paths:
        return max(paths, key=lambda path:len(path))
    else:
        return ''
    
    
#Step3
###Putting it together
def longest_absolute_path(s):
    return len(longest_path(build_fs(s)))