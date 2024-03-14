# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = []
        def dfs(node, s):
            if not node.left and not node.right:
                res = s + str(node.val)
                total.append(int(res))
            if node.left:
                dfs(node.left, str(s) + str(node.val))
            if node.right:
                dfs(node.right, str(s) + str(node.val))
        dfs(root, "")
        return sum(total)