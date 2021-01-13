# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:06:29 2020

@author: Satyam Patidar MCS20026
"""


class nestedDict:
    def __init__(self):
        self.qDict = {'a':{'A'}, 'b':{'bb':'BB'}, 'c':{'C'}, 'd':{'dd':''}}
        
    def add(self, key, value):
        self.qDict[key] = value
    
    def delete(self, key):
        if key in self.qDict:
            self.qDict.pop(key)