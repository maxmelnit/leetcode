# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Construct a list in-order, and check if it's in ascending order

        ordered = []

        def dfs(root):

            nonlocal ordered

            if root is None:
                return

            # In-order traversal
            dfs(root.left)
            ordered.append(root.val)
            dfs(root.right)

        dfs(root)

        for i in range(len(ordered) - 1):
            if not ordered[i] < ordered[i + 1]:
                return False

        return True

