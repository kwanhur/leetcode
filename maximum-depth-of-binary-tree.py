#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
            

if __name__ == '__main__':
    so = Solution()


    def test():
        root = TreeNode(1)
        assert so.maxDepth(root) == 1

        root.left = TreeNode(2)
        assert so.maxDepth(root) == 2
        root.left.right = TreeNode(3)
        assert so.maxDepth(root) == 3

        root.left.right = None
        root.right = TreeNode(2)
        assert so.maxDepth(root) == 2
        root.right = TreeNode(3)
        assert so.maxDepth(root) == 2

        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        assert so.maxDepth(root) == 3

        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        assert so.maxDepth(root) == 3


    test()
