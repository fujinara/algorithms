# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def maxPathSum(root):
    res = root.val

    def dfs(root):
        nonlocal res
        if not root:
            return 0
        leftMax = max(0, dfs(root.left))
        rightMax = max(0, dfs(root.right))
        # with split at root
        res = max(res, leftMax + rightMax + root.val)
        # without split at root
        return max(leftMax, rightMax) + root.val
    
    dfs(root)
    return res