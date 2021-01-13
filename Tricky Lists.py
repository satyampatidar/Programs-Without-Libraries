# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:09:29 2020

@author: Satyam Patidar MCS20026

A function checkList(inList) that takes in a list that contains already filled values, similar to the ones given below.
You need to write a function whether the list contains, numbers in a sequence or not, if the sequence is not followed it should return the inner list that does not follow the sequence or
It should return True.
The sequence could be either odd or even numbers as shown below.
Note: only one level of depth is expected to be handled.
Sample inputs which are correctly filled are given below:
Input1: [[0], [2, 4]]
Input2: [[1], [3, 5], [7, 9, 11]]
Input3: [[1], [3, 5], [7, 9, 11], [13, 15, 17, 19], [21, 23, 25, 27, 29]]
InPut4: [[0], [2, 4], [6, 8, 10], [12, 14, 16, 18]]


"""

def checkList(inList):
    n = len(inList)
    if n%2==0:
        e = 0
        for i in range(n):
            l = inList[i]
            for j in range(len(l)):
                if l[j] != e:
                    return l
                e += 2
    else:
        e = 1
        for i in range(n):
            l = inList[i]
            for j in range(len(l)):
                if l[j] != e:
                    return l
                e += 2
    return True


checkList([[1], [3, 5], [7, 9, 11], [13, 15, 17, 19], [21, 23, 25, 27, 29]])
            