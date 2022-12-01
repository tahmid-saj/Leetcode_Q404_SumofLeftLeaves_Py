# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.sum = 0
        
        def function(root,x):
            if not root.left and not root.right:
                if x == 'left':
                    self.sum += root.val
            if root.left:
                function(root.left, "left")
            if root.right:
                function(root.right, "right")
        
        function(root, "")
        
        return self.sum
