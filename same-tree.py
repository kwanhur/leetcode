#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False


        if self.isSameTree(p.left, q.left):
            return self.isSameTree(p.right, q.right)
        else:
            return False

def gen_tree(nums):
    for i, n in enumerate(nums):
        node = TreeNode(n)
        nums[i] = node

    root = nums[0]

if __name__ == '__main__':
    so = Solution()

    def test():
        pass

    test()

