# https://leetcode.com/problems/maximum-subarray/

# Maximum Subarray

# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.



#Sol 1: Brute Force

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l1 = []
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                result = sum(nums[i:j+1])
                l1.append(result)
        return max(l1)


#Sol 2:  

# kadane's Algorithm

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l1 = []
        max_total = max_current = nums[0] 
        n = len(nums)
        for i in range(1,n):
            max_current = max(nums[i], max_current+nums[i])
            if max_current > max_total:
                max_total = max_current
        return max_total
