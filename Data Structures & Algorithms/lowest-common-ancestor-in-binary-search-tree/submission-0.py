# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root, p, q):

            if root is None:
                return None

            # Split case (root is the lowest common ancestor)
            if p.val > root.val > q.val or p.val < root.val < q.val:
                return root

            if root.val == p.val or root.val == q.val:
                return root

            # Look in the left subtree
            if root.val > p.val and root.val > q.val:
                return dfs(root.left, p, q)

            # Look in right subtree
            if root.val < p.val and root.val < q.val:
                return dfs(root.right, p, q)

        return dfs(root, p, q)

            