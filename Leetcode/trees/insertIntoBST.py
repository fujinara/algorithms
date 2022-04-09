# https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    if val > root.val:
        root.right = insertIntoBST(root.right, val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    return root