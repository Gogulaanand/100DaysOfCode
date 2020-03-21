# Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Given a binary tree, find its maximum depth.
# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
# Note: A leaf is a node with no children.
# Example:

# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its depth = 3.

#Sol 1:
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = [1]
        def dive(root: TreeNode, level: int, depth: list) -> int:
            if root==None:
                return
            depth[0] = max(depth[0], level)
            dive(root.left, level+1, depth)
            dive(root.right, level+1, depth)
            return depth
        return dive(root, 1, depth)[0]


# Sol 2: counting from downwards

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        left_child_height = self.maxDepth(root.left)
        right_child_height = self.maxDepth(root.right)
        return max(left_child_height, right_child_height)+1

