#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        ret = []
        if not root:
            return ret

        if root.left:
            res = self.inorderTraversal(root.left)
            ret.extend(res)
        ret.append(root.val)
        if root.right:
            res = self.inorderTraversal(root.right)
            ret.extend(res)
        return ret


if __name__ == '__main__':
    so = Solution()

    def test():
        root = TreeNode(1)
        n2 = TreeNode(2)
        root.right = n2
        n3 = TreeNode(3)
        n2.left = n3
        print so.inorderTraversal(root)

    test()

