"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        q = deque([root])
        depth = 0
        while q:
            level_size = len(q)
            for _ in range(level_size):
                current = q.popleft()
                if current.children:
                    for n in current.children:
                        q.append(n)
            depth += 1
        return depth
