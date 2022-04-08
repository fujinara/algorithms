# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections

def levelOrder(root):
    if not root:
        return []
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        levelSize = len(q)
        level = []
        for i in range(levelSize):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    
    return res