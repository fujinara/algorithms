# https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import collections

def rightSideView(root):
    if not root:
        return []
    res = []
    q = collections.deque()
    q.append(root)

    while q:
        levelSize = len(q)
        for i in range(levelSize):
            node = q.popleft()
            if i == levelSize - 1:
                res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    return res