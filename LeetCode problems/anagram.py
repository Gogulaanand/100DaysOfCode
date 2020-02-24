# https://leetcode.com/problems/valid-anagram/

# Valid Anagram


# Given two strings s and t , write a function to determine if t is an anagram of s.

# Input: s = "anagram", t = "nagaram"
# Output: true


# Sol 1:
#Runtime: 28 ms, faster than 99.27% of Python3 online submissions for Valid Anagram.
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = list(set(s))
        tt = list(set(t))
        if len(ss)!=len(tt):
            return False
        else:
            for item in ss:
                if s.count(item) == t.count(item):
                    continue
                else:
                    return False
            return True

#Sol 2:
#inbuilt counter function

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s)==collections.Counter(t)
