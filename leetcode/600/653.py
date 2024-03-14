# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        val = set()
        q = deque([root])
        while q:
            current = q.popleft()
            for n in val:
                if (n+current.val) == k:
                    return True
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            val.add(current.val)
        return False