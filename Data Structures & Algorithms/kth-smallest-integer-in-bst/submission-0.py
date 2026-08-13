# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        in_order = []
        # Basically, build a list with in-order traversal and then select the kth element (1-indexed)

        def dfs(root):

            if root is None:
                return

            dfs(root.left)
            in_order.append(root)
            dfs(root.right)

            return

        dfs(root)
        return in_order[k - 1].val

            