#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def permute(self, nums):
        if not nums:
            return []

        def arrange(nums0, total):
            if total == 1:
                return [nums0]

            ret, t = [], total - 1
            for i, v in enumerate(nums0):
                res = arrange(nums0[:i] + nums0[i + 1:], t) #[[...],[...]]
                v = [v]
                for item in res:
                    ret.append(v + item)
            return ret


        return arrange(nums, len(nums))


if __name__ == '__main__':
    so = Solution()

    def test(nums):
        print 'nums:',nums,' ret:\n', len(so.permute(nums))

    test([1])
    test([1, 2])
    test([1, 2, 3])
    test([0, 1, 2, 3])
    test([-1, 0, 1, 2, 3])
    test([1, 2, 3,4,5,6])
