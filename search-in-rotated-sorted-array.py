#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        return nums.index(target)

    def search2(self, nums, target):
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right and len(nums[left: right + 1]) > 0:
            if nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            else:
                left, right = left + 1, right - 1
        return -1


if __name__ == '__main__':
    so = Solution()
    assert (so.search([4,5,6,7,0,1,2], 0) == 4)
    assert (so.search([4,5,6,7,0,1,2], 3) == -1)

