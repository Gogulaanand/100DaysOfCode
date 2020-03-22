# Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors.

# If there is no such integer in the array, return 0.

 

# Example 1:

# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.


from functools import reduce
class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def factor(n):
            return set(reduce(list.__add__, [[i, n//i] for i in range(1, int(n**0.5)+1) if not n%i]))
        
        total = 0
        for num in nums:
            f = factor(num)
            if len(f)==4:
                total += sum(f)
        return total