# A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).

# Given a string s. Return the longest happy prefix of s .

# Return an empty string if no such prefix exists.

# Example 1:

# Input: s = "level"
# Output: "l"
# Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".

# Example 2:

# Input: s = "ababab"
# Output: "abab"
# Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.

# Example 3:

# Input: s = "leetcodeleet"
# Output: "leet"

# Example 4:

# Input: s = "a"
# Output: ""


#Sol 1:
class Solution:
    def longestPrefix(self, s: str) -> str:
        x = list(s)
        length = len(x)
        if length==1:
            return ''
        y = x[:]
        for i in range(1, length):
            yy = ''.join(y[i:])
            xx = ''.join(x[:-i])
            if xx==yy:
                return xx
        return ''



#Sol 2: brute force
class Solution:
    def longestPrefix(self, s: str) -> str:
        l1 = []
        l2 = []
        x = list(s)
        length = len(x)
        if length==1:
            return ''
        y = (x[:])[::-1]
        for i in range(1, length):
            l1.append(''.join(x[:i]))
            l2.append(''.join(y[:i][::-1]))
        res = []
        for a in l1:
            if a in l2:
                res.append(a)
        if res:
            return max(res)
        else:
            return ''