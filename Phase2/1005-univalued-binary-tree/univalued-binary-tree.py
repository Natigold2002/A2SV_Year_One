# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        visited = set()
        comp = root.val
        queue.append(root)
        # node= root
        while queue:
            node = queue.popleft()

            if node and node.val != comp:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return True
            