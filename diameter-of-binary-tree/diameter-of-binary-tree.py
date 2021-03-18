# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.max_res = 0
        def DFS(root):
            if not root:
                return 0 
            left = DFS(root.left)
            right = DFS(root.right)
            self.max_res = max(self.max_res, left + right + 1)
            return max(left, right) + 1
        
        DFS(root)
        return self.max_res - 1