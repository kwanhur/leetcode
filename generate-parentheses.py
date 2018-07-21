#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def generateParenthesis(self, n):
        if n <= 0:
            return []
        if n == 1:
            return ['()']

        res = self.generateParenthesis(n - 1)
        ret = set()
        for v in res:
            for i in range(len(v)):
                ret.add(v[0: i] + '()' + v[i:])
        return list(ret)


if __name__ == '__main__':
    so = Solution()
    # assert (so.generateParenthesis(0) == [])
    # assert (so.generateParenthesis(1) == ['()'])
    # print so.generateParenthesis(2)
    a = so.generateParenthesis(3)
    print 'n:3 sum:', len(a)
    a = so.generateParenthesis(4)
    print 'n:4 sum:', len(a)
    a = so.generateParenthesis(5)
    print 'n:5 sum:', len(a)
    a = so.generateParenthesis(6)
    print 'n:6 sum:', len(a)
