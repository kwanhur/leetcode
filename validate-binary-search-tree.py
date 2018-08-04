#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        左子树所有值必需小于根
        友子树所有值必需大于根
        中序遍历,左根右,合法二叉树 必然成为ASC排列
        """
        if not root or (not root.left and not root.right):
            return True

        def fetch(node):
            ret = []
            if node.left:
                res = fetch(node.left)
                ret.extend(res)
            ret.append(node.val)
            if node.right:
                res = fetch(node.right)
                ret.extend(res)
            return ret

        res = fetch(root)
        i = 0
        while i < len(res) - 1:
            if res[i] >= res[i + 1]:
                return False
            i += 1
        return True


if __name__ == '__main__':
    so = Solution()

    root = TreeNode(5)
    root.left = TreeNode(1)
    n2 = TreeNode(4)
    root.right = n2
    n2.left = TreeNode(3)
    n2.right = TreeNode(6)

    assert so.isValidBST(root) == False

    root = TreeNode(0)
    root.left = TreeNode(1)
    assert so.isValidBST(root) == False

    root = TreeNode(0)
    root.right = TreeNode(-1)
    assert so.isValidBST(root) == False

    root = TreeNode(1)
    root.left = TreeNode(1)
    assert so.isValidBST(root) == False

    root = TreeNode(1)
    assert so.isValidBST(root)

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    assert not so.isValidBST(root)

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    assert not so.isValidBST(root)

    root = TreeNode(3)
    root.right = TreeNode(5)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    assert so.isValidBST(root)
