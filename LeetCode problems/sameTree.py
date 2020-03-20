# https://leetcode.com/problems/same-tree/

# Same Tree
# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

#Sol 1: DFS

l1, l2 = [], []
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
        return (dfs(p, l1) == dfs(q, l2))