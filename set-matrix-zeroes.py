#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def setZeroes(self, matrix):
        if not matrix:
            return

        cols = set()
        for i, row in enumerate(matrix):
            if row.count(0) > 0:
                for j, col in enumerate(row):
                    if not col:
                        cols.add(j)
                matrix[i] = [0] * len(row)
        for j in cols:
            for row in matrix:
                    row[j] = 0


if __name__ == '__main__':
    so = Solution()


    def test(m):
        print 'origin:'
        print m
        so.setZeroes(m)
        print 'ret:'
        print m


    test([
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ])

    test([
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ])
