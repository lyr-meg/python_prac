# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, maxVal):
            if not node:
                return 0
            
            if node.val >= maxVal:
                res=1
                maxVal = node.val
            else:
                res=0

            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)
        
            return res

        return dfs(root, root.val)
    
# time complexity: O(n) because we visit each node once
# space complexity: O(h) where h is the height of the tree, due to the recursion stack