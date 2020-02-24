# https://leetcode.com/problems/product-of-array-except-self/

# Product of Array Except Self

# Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Input:  [1,2,3,4]
# Output: [24,12,8,6]


#Sol 1: (brute force)

from functools import reduce
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            list_copy = nums[:]
            list_copy.pop(i)
            list_copy = list(filter((1).__ne__, list_copy))
            list_copy.append(1)
            l.append(reduce((lambda x,y:x*y), list_copy))
        return l

#Sol 2: