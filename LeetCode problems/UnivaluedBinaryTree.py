# Univalued Binary Tree
# https://leetcode.com/problems/univalued-binary-tree/
# A binary tree is univalued if every node in the tree has the same value.

# Return true if and only if the given tree is univalued.


#Sol 1: iterative BFS
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        l = [root.val]
        queue = [root]
        while(queue):
            current = queue.pop(0)
            if current.val!=l[-1]:
                return False
            else:
                l.append(current.val)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        l.pop(0)
        if len(l) == l.count(l[0]):
            return True
        else:
            return False

#Sol 2: recursive DFS

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        def dfs(node: TreeNode) -> bool:
            return node is None or node.val == root.val and dfs(node.left) and dfs(node.right)
        return dfs(root)