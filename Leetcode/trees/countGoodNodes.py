# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def goodNodes(root):

    def dfs(root, maxVal):
        if not root:
            return 0
        res = 1 if root.val >= maxVal else 0
        maxVal = max(maxVal, root.val)
        res += dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return res
    
    return dfs(root, root.val)