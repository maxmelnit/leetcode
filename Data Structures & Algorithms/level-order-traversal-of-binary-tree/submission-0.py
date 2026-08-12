# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            level = []
            q_len = len(q)

            for _ in range(q_len):
                popped = q.popleft()
                level.append(popped.val)

                if popped.left != None:
                    q.append(popped.left)

                if popped.right != None:
                    q.append(popped.right)

            res.append(level)


        return res

            