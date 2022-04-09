# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def searchBST(root, val):
    if root is None:
        return None
    if val > root.val:
        return searchBST(root.right, val)
    if val < root.val:
        return searchBST(root.left, val)
    return root