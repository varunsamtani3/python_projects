#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:51:09 2019

@author: varunsamtani
"""
from typing import List

class Solution:
    
    def getRange(self, n1, n2):
        if (n1 == n2):
            return str(n1)
        
        else:
            return "{}->{}".format(str(n1), str(n2))    
    
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        res = []
          
        #the next number we need to find
        next_val = lower;
      
        for i in range(len(nums)):
            #not within the range yet
            if (nums[i] < next_val):
                continue
        
            #continue to find the next one
            if (nums[i] == next_val):
                next_val += 1
                continue
        
            #get the missing range string format
            res.append(self.getRange(next_val, nums[i]-1));
        
            #now we need to find the next number
            next_val = nums[i] + 1;
          
        #do a final check
        if (next_val <= upper):
            res.append(self.getRange(next_val, upper))
        
        return res