#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def maxSubArray(self, nums):
        """
        动态规划：s = max(s+nums[i], nums[i])
        s是前面N项的和，若加一项小于当前值，则重置s的起始边界为i
        """
        if not nums:
            return

        s, m = 0, sum(nums)
        for i in range(len(nums)):
            if s + nums[i] < nums[i]:
                s = nums[i]
            else:
                s += nums[i]
            if s > m:
                m = s

        return m


if __name__ == '__main__':
    so = Solution()

    def test(nums):
        n = so.maxSubArray(nums)
        print 'nums:', nums,' ret:', n
        return n

    test([-2,1,-3,4,-1,2,1,-5,4])
    test([-2,1,-3,3,-1,2,1,-5,4])
    test([-2])
    assert test([-2, 1]) == 1
    assert test([1, -2]) == 1
    test([-3,-2,-1])
    test([1,2,3])
    test([-1,0,1])
    test([-1,0,1,2,3,1])

