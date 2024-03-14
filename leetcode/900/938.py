from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque()
        q.append(root)
        sum = 0
        while q:
            current = q.popleft()
            if low <= current.val and current.val <= high:
                sum += current.val
            if current.left is not None:
                q.append(current.left)
            if current.right is not None:
                q.append(current.right)
        return sum