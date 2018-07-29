#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def generateMatrix(self, n):
        if n <= 0:
            return []

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        r1, r2, c1, c2 = 0, n - 1, 0, n - 1
        n0, t = 1, n * n
        while True:
            for c in range(c1, c2 + 1):
                matrix[r1][c], n0 = n0, n0 + 1
            if n0 > t:
                break
            r1 += 1
            for r in range(r1, r2 + 1):
                matrix[r][c2], n0 = n0, n0 + 1
            if n0 > t:
                break
            c2 -= 1
            for c in range(c2, c1 - 1, -1):
                matrix[r2][c], n0 = n0, n0 + 1
            if n0 > t:
                break
            r2 -= 1
            for r in range(r2, r1 - 1, -1):
                matrix[r][c1], n0 = n0, n0 + 1
            if n0 > t:
                break
            c1 += 1

        return matrix


if __name__ == '__main__':
    so = Solution()


    def test(n):
        print 'n:', n, 'ret:'
        m = so.generateMatrix(n)
        for r in m:
            print r


    test(0)
    test(1)
    test(2)
    test(3)
    test(4)
    test(5)
    test(6)
    test(7)
    test(8)
    test(9)
    test(10)
