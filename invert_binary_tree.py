#! /usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kwanhur'

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root:
            return
        root.left = self.invertTree(root.left)
        root.right = self.invertTree(root.right)

        tmp_node = root.left
        root.left = root.right
        root.right = tmp_node

        return root


if __name__ == '__main__':
    root = TreeNode(1)
    solution = Solution()
    tree = solution.invertTree(root)
    print(tree)
