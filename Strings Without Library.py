# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 19:22:42 2020

@author: Satyam Patidar MCS20026
"""

class myStringCls:
    def len(self, s):
        i = 0
        for c in s:
            i += 1
        return i
    
    def addStr(self,s1,s2):
        s = ''
        for c in s1:
            s += c
        for c in s2:
            s += c
        return s
    
    def cmpStr(self, s1, s2):
        if self.len(s1) == self.len(s2):
            n = self.len(s1)
            for i in range(n):
                if s1[i] != s2[i]:
                    return False
        else:
            return False
        return True
    
    def isItNullStr(self, s):
        if s=='':
            return True
        else:
            return False
            

