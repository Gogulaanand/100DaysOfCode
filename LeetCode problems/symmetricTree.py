# https://leetcode.com/problems/symmetric-tree/
# Symmetric Tree

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3

 

# But the following [1,2,2,null,3,null,3] is not:

#     1
#    / \
#   2   2
#    \   \
#    3    3


#Sol 1:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode, l: list) -> list:
            if node == None: 
                return []
            dfs(node.left, l)
            if (node.left ==None and node.right!=None):
                l.append(None)
                l.append(node.val)
            elif (node.right==None and node.left!=None):
                l.append(node.val)
                l.append(None)
            else:
                l.append(node.val)
            dfs(node.right, l)
            return l
        in_order = dfs(root, [])
        if len(in_order)==0:
            return True
        mid = len(in_order)//2
        left_sub_tree = in_order[:mid]
        right_sub_tree_reversed = in_order[mid+1:][::-1]
        return left_sub_tree == right_sub_tree_reversed



#Sol 2:
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)
    
    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            outer = self.isMirror(left.left, right.right)
            inner = self.isMirror(left.right, right.left)
            return outer and inner
        else:
            return False