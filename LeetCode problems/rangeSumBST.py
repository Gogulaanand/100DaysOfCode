# Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
# Given the root node of a binary search tree, return the sum of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.

# Example 1:

# Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
# Output: 32

class Solution:  
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        queue = [root]
        total = 0
        while(queue):
            current = queue.pop(0)
            if(L <= current.val <=R):
                total+=current.val
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            elif current.val<L:
                if current.right is not None:
                    queue.append(current.right)
            else:
                if current.left is not None:
                    queue.append(current.left)             
        return total