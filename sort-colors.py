#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def sortColors(self, nums):
        if not nums:
            return nums
        i, j = 0, len(nums) - 1
        for v in nums[:]:
            if v == 0:
                nums[i], i = 0, i + 1
            elif v == 2:
                nums[j], j = 2, j - 1
        nums[i: j + 1] = [1] * (j - i + 1)

if __name__ == '__main__':
    so = Solution()

    def test(n):
        print 'ori:', n, ' ret:'
        so.sortColors(n)
        print n

    test([2,0,2,1,1,0])
    test([0,0,1,1,2,2,2,1,1,1,0,0,2])
