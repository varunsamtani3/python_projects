#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 13:19:23 2019

@author: varunsamtani
"""

### Slowest solution, brute force
class Solution:
    
    def isUnique(self, s, start, stop) -> bool:
        uniqueSet = set()
        for i in range(start, stop):
            if s[i] in uniqueSet:
                return False
            uniqueSet.add(s[i])
            
        return True
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        length = len(s)
        max_length = 0
        
        for i in range(length):
            for j in range(i+1, length+1):
                if self.isUnique(s, i, j):
                    max_length = max(max_length, j-i)
                    
        return max_length
    
    
### Vanilla Sliding window approach
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = stop = maxLength = 0
        usedChar = set()
        
        while((start < len(s)) and (stop < len(s))):
            if s[stop] not in usedChar:
                usedChar.add(s[stop])
                stop += 1
                maxLength = max(maxLength, stop - start)
                
            else:
                usedChar.remove(s[start])
                start += 1
                
        return maxLength
            
        
    
### Optimized Sliding window approach
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        start = maxLength = 0
        usedChar = {}
        
        for stop in range(len(s)):
            if s[stop] in usedChar and start <= usedChar[s[stop]]:
                start = usedChar[s[stop]] + 1
            else:
                maxLength = max(maxLength, stop - start + 1)

            usedChar[s[stop]] = stop

        return maxLength
        