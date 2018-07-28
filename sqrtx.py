#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def newTonSqrt(self, x):
        """
        牛顿迭代法
        """
        if x <= 0:
            return 0
        res = x
        while True:
            last = res
            res = (res + x / res) / 2.0

            if abs(last - res) < 1:
                break
        return int(res)

    def mySqrt(self, x):
        """
        二分法 逼近查找，精度为小于1
        """
        if x <= 0:
            return 0

        left, right = 1, x / 2 + 1
        mid = left + (right - left) / 2 + 1
        while True:
            n = mid ** 2
            if n > x:
                right = mid
            elif n == x:
                return mid
            else:
                left = mid
            last = mid
            mid = left + (right - left) / 2

            if abs(last - mid) < 1:
                break
        return mid


if __name__ == '__main__':
    so = Solution()


    def test(x):
        print 'origin:', x, 'ret:', so.newTonSqrt(x)


    test(1)
    test(2)
    test(3)
    test(4)
    test(5)
    test(7)
    test(9)
    test(11)
    test(16)
    test(20)
    test(100)
    test(30)
    test(36)
    test(48)
    test(63)
    test(80)
    test(97)
    test(200)
    test(400)
