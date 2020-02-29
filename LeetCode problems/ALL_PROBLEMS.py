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