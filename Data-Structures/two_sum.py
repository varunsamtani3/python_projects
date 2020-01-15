#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:14:42 2019

@author: varunsamtani
"""
from typing import List

### brute force solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        twosum_pair = []
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                
                if nums[j] == target - nums[i]:
                    twosum_pair.append(i)
                    twosum_pair.append(j)
                    return twosum_pair
                
        if len(twosum_pair) == 0:
            return None
                    
                
### using hash table, with two passes through list
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        valsDict = {}
        
        for i in range(len(nums)):
            valsDict[nums[i]] = i
            
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in valsDict and valsDict[complement] != i:
                return [i, valsDict[complement]]
            
            
            
### using hash table, with one pass through list
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        valsDict = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in valsDict:
                return [i, valsDict[complement]]  
            valsDict[nums[i]] = i
            
        return [-1,-1]