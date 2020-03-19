# Leaf-Similar Trees
# https://leetcode.com/problems/leaf-similar-trees/


#Sol 1: DFS
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(node: TreeNode, l: List) -> bool:
            if node is None:
                return 
            if node.left is None and node.right is None:
                l.append(node.val)
                return l
            dfs(node.left, l)
            dfs(node.right, l)
            return l
        return dfs(root1, []) == dfs(root2, [])