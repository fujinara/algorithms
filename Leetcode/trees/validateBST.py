# https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isValidBST(root):
    
    def dfs(root, leftBound, rightBound):
        if not root:
            return True
        if leftBound >= root.val or rightBound <= root.val:
            return False
        return dfs(root.left, leftBound, root.val) and dfs(root.right, root.val, rightBound)

    return dfs(root, float('-inf'), float('inf'))