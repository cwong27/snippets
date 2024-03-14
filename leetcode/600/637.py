# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        depth = 0
        q = deque([root])
        while q:
            level_size = len(q)
            node_sum = 0
            for _ in range(level_size):
                node = q.popleft()
                node_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(round(node_sum/level_size, 5))
            depth += 1
        return res