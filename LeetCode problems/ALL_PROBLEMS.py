# https://leetcode.com/problems/non-overlapping-intervals/

# Non-overlapping Intervals

# Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

# Example 1:

# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.


# Sol:

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