#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        遍历数组,每出栈一个元素判断是否存在子节点并压栈
        """
        if not root:
            return []

        s, ret = [root], []
        while s:
            l = []
            for i in range(len(s)):  # 当前层所有元素个数,出栈对应次数
                n = s.pop(0)
                l.append(n.val)
                if n.left:
                    s.append(n.left)
                if n.right:
                    s.append(n.right)

            ret.append(l)
        return ret[::-1]

    def levelOrderBottom2(self, root):
        if not root:
            return []
        ret = {}

        def bfs(node, level):
            if level not in ret:
                ret[level] = []
            ret[level].append(node.val)
            if node.left:
                bfs(node.left, 1 + level)
            if node.right:
                bfs(node.right, 1 + level)

        bfs(root, 1)
        ret = map(lambda x: x[1], sorted(ret.items(), key=lambda x: x[0], reverse=True))

        return ret


if __name__ == '__main__':
    so = Solution()


    def test():
        root = TreeNode(1)
        n2 = TreeNode(2)
        root.right = n2
        root.left = TreeNode(0)
        n3 = TreeNode(3)
        n2.left = n3
        n2.right = TreeNode(4)
        n2.left.left = TreeNode(10)
        print so.levelOrderBottom(root)


    test()
