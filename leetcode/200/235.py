# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(node, p, q):
            if min(p, q) < node.val and node.val < max(p, q):
                return node
            if node.val == p or node.val == q:
                return node
            if p < node.val and q < node.val:
                return lca(node.left, p, q) 
            if node.val < p and node.val < q:
                return lca(node.right, p, q)
        return lca(root, p.val, q.val)