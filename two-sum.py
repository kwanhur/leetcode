#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import operator

class Solution(object):
    """
    https://leetcode-cn.com/problems/two-sum/description/
    """
    def add(self, nums):
        return operator.add(nums[0], nums[1])

    def twoSum(self, nums, target):
        ret =  {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in ret:
                return [ret[num], i]
            else:
                ret[nums[i]] = i
        return

    def twoSum1(self, nums, target):
        if not nums or target is None:
            return

        if len(nums) == 2 and self.add(nums) == target:
            return [0, 1]
        else:
            for i, a in enumerate(nums):
                nums2 = nums[i+1:]
                num = target - a
                for j, b in enumerate(nums2):
                    if b == num:
                        return [i, i + j + 1]
            return 


if __name__ == '__main__':
    so = Solution()
    print so.twoSum([2, 7, 11, 15], 9)
    print so.twoSum([2, 7, 11, 15], 17)
    print so.twoSum([2, 7, 11, 15], 0)
    print so.twoSum([], 0)

