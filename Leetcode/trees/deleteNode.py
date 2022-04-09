# https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def deleteNode(root, key):
    if not root:
        return root
    if root.val > key:
        root.left = deleteNode(root.left, key)
    elif root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        temp = root.right
        while temp.left:
            temp = temp.left
        root.val = temp.val
        root.right = deleteNode(root.right,root.val)
    return root