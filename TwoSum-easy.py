"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
"""

class Solution(object):
    def twoSum(self, nums, target)
        for i in range(len(nums)):
            if target-nums[i] in nums:
                j=nums.index(target-nums[i])
                if i!=j:
                    break
                
        return [i,j]   
