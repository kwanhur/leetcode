#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def combine2(self, n, k):
        if k > n or n < 1:
            return []

        ret = []

        def bine(res, start):
            if len(res) == k:
                ret.append(res)
                return

            for i in xrange(start, n + 1):
                bine(res + [i], i + 1)

        bine([], 1)

        return ret

    def combine(self, n, k):
        if k > n or n < 1:
            return []

        def bine(nums, total):
            if total == 1:
                return [[i] for i in nums]
            else:
                ret = []
                for i, v in enumerate(nums):
                    v = [v]
                    res = bine(nums[i + 1:], total - 1)
                    for r in res:
                        ret.append(v + r)
                return ret

        return bine([i for i in xrange(1, n + 1)], k)


if __name__ == '__main__':
    so = Solution()


    def test(n, k):
        print 'n:', n, ' k:', k, ' ret:'
        for r in so.combine(n, k):
            print r


    test(4, 2)
    test(4, 4)
    test(7, 5)
    test(10, 9)
