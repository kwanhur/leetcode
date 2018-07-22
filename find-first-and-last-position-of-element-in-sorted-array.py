#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def searchRange(self, nums, target):
        c = nums.count(target)
        if not c:
            return [-1, -1]
        first, last = nums.index(target), -1
        nums2 = nums[::-1]
        last = len(nums) - nums2.index(target) - 1
        return [first, last]


if __name__ == '__main__':
    so = Solution()
    assert (so.searchRange([5,7,7,8,8,10], 8) == [3, 4])
    assert (so.searchRange([5,7,7,8,8,10], 6) == [-1, -1])
    assert (so.searchRange([5,7,7,8,8,10], 5) == [0, 0])
    assert (so.searchRange([1], 1) == [0, 0])
