# https://leetcode.com/problems/binary-tree-right-side-view/description/
# Difficulty: Medium

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.
'''

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []

        res = []

        q = deque()
        q.append(root)

        while q:
            level = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
            res.append(level[-1])

        return res




        