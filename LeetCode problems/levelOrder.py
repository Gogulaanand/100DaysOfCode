# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

# For example:
# Given binary tree [3,9,20,null,null,15,7],

#     3
#    / \
#   9  20
#     /  \
#    15   7

# return its bottom-up level order traversal as:

# [
#   [15,7],
#   [9,20],
#   [3]
# ]


#Sol 1:
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.dfs(root, 0, res)
        return res[::-1]
    
    def dfs(self, root: TreeNode, level: int, res: list) -> List[List[int]]:
        if root:
            if len(res)<(level+1):
                res.append([])
            res[level].append(root.val)
            self.dfs(root.left, level+1, res)
            self.dfs(root.right, level+1, res)




#Sol 2: (not so perfect)
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        result = []
        queue = [root,'br']
        l = []
        if root is None:
            return []
        while(queue):
            current = queue.pop(0)
            if current=="br":
                result.insert(0,(l[:]))
                l.clear()
                if len(q)%2!=0 and q[-1]!='br':
                    queue.append("br")
                continue
            else:
                l.append(current.val)
            if len(queue)%2!=0 and queue[-1]!='br':
                queue.append("br")
            if current.left is None and current.right is None and len(queue)==0:
                result.insert(0, l[:])
                continue
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
        return result