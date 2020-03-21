# https://leetcode.com/problems/same-tree/
# Same Tree
# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.


# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true

# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false

# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false

#Sol 1: DFS

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(node: TreeNode, l: List) -> bool:
            if node is None:
                return
            if node.left is None and node.right is not None:
                l.append(None)
            else:
                l.append(node.val)
            dfs(node.left, l)
            dfs(node.right, l)
            return l
        return (dfs(p, []) == dfs(q, []))


# Sol 2:
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True
        elif (p == None and q != None) or (p!=None and q==None):
            return False
        elif p.val==q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False



# Sol 3:

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q