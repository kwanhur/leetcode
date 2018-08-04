#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False

        ret = False
        for row in matrix:
            if not row or row[0] > target:
                return ret
            elif row[-1] >= target:
                ret = target in row
        return ret


if __name__ == '__main__':
    so = Solution()

    def test(m, t):
        print 'target:', t, ' ori:'
        for i in m:
            print i
        print 'ret:', so.searchMatrix(m, t)

    test([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3)

    test([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13)
