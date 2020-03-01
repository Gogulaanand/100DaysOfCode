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






