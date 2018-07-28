#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def climbStairs(self, n):
        if n <= 2:
            return n

        c1, c2 = 1, 2 # 1 for One stair, 2 for Two stairs
        for i in range(3, n + 1):
            c1, c2 = c2, c1 + c2
        return c2
            

if __name__ == '__main__':
    so = Solution()

    def test(n):
        print 'n:', n, 'way:', so.climbStairs(n)

    test(1)
    test(2)
    test(3)
    test(4)
    test(5)
    test(10)

