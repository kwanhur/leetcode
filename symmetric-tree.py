#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def valid(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            return left.val == right.val and valid(left.left, right.right) and valid(left.right, right.left)

        return valid(root.left, root.right)

if __name__ == '__main__':
    so = Solution()


    def test():
        root = TreeNode(1)
        assert so.isSymmetric(root)

        root.left = TreeNode(2)
        assert not so.isSymmetric(root)
        root.right = TreeNode(2)
        assert so.isSymmetric(root)
        root.right = TreeNode(3)
        assert not so.isSymmetric(root)

        root.left = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right = TreeNode(3)
        root.right.left = TreeNode(2)
        assert not so.isSymmetric(root)

        root.left = TreeNode(2)
        root.right = TreeNode(2)
        root.left.left = TreeNode(3)
        root.right.right = TreeNode(3)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(4)
        assert so.isSymmetric(root)


    test()
