# https://leetcode.com/problems/non-overlapping-intervals/

# Non-overlapping Intervals

# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

# Solution:
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        length = len(intervals)
        if length==0 or length==1:
            return 0
        out = []
        for i in sorted(intervals, key=lambda i: i[1]):
            if out and i[0] < out[-1][1]:
                continue
            else:
                out.append(i)
        return length-len(out)




# https://leetcode.com/problems/valid-parentheses/
# Valid Parentheses
#Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        elif len(s)==1:
            return False
        pairs = {'(':')','[':']','{':'}'}
        open = ['(','[','{']
        close = [')',']','}']
        l=[]
        for item in s:
            if item in open:
                l.append(item)
            elif item in close:
                if l and pairs[l[-1]]==item:
                    l.pop()
                else:
                    return False
        if len(l)==0:
            return True
        else:
            return False



# Two sum problem:
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Sol 1: O(n2)  Brute-force approach

nums = [0, 12, 5, 7]
target = 12
flag = False
for i in range(len(nums)):
    current = nums[i]
    l = nums[:]
    l.pop(i)
    for item in l:
        if item+current==target:
            flag=True
            break
    if(flag==True):
        break
print(flag)


#Sol 2:
#still O(n2)
nums = [1, 12, 5, 7]
target = 14
flag = False
for i in range(len(nums)):
    current = nums[i]
    diff = target-current
    if diff>0 and (diff in nums[i+1:] or diff in nums[0:i]):
        flag = True
        break
print(flag)


#Sol3: O(n)
def twoSum(num_array, sum):
    nums = num_array
    target = sum
    dict = {}
    for i in range(len(nums)):
        current = nums[i]
        if current in dict:
            return True
        else:
            dict[target-nums[i]] = nums[i]

assert twoSum([10,2,7,5],15)
assert not twoSum([1,1,2,3],6)
assert twoSum([10,8,12,8],16)




# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
# How Many Numbers Are Smaller Than the Current Number

# Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

# Return the answer in an array.

# Example 1:

# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

# Sol 1: (Brute-force)

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        out = []
        for i in range(len(nums)):
            l = nums[:]
            l.pop(i)
            current = nums[i]
            count = 0
            for item in l:
                if item<current and item!=current:
                    count+=1
            out.append(count)
        return out




# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
# Number of Steps to Reduce a Number to Zero

# Given a non-negative integer num, return the number of steps to reduce it to zero. If the current number is even, you have to divide it by 2, otherwise, you have to subtract 1 from it.

# Example 1:

# Input: num = 14
# Output: 6
# Explanation:
# Step 1) 14 is even; divide by 2 and obtain 7.
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3.
# Step 4) 3 is odd; subtract 1 and obtain 2.
# Step 5) 2 is even; divide by 2 and obtain 1.
# Step 6) 1 is odd; subtract 1 and obtain 0.

# Sol:

class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        while num!=0:
            if num%2==0:
                num/=2
            else:
                num-=1
            count+=1
        return count
