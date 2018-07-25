#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def rotate2(self, matrix):
        """
        rotate rows r0<->r(n-1)
        zip combine first element at rows
        map-list convert to list and return list
        list[:] means start = 0, end = n, step = 1, then every element will update by map result
        """
        matrix[:] = map(list, zip(*matrix[::-1]))

    def rotate(self, matrix):
        n = len(matrix)
        if not n:
            return matrix

        # rotate rows
        for i, r in enumerate(matrix):
            matrix[i] = r[::-1]

        for i in range(n):
            for j in range(n - i):
                tr, tc = n - 1 - j, n - 1 - i
                matrix[i][j], matrix[tr][tc] = matrix[tr][tc], matrix[i][j]


if __name__ == '__main__':
    so = Solution()


    def test(m):
        print 'origin:\n', m, '\nresult:\n'
        so.rotate(m)
        print m


    l = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16]
    ]
    test(l)
    l = [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ]
    test(l)
