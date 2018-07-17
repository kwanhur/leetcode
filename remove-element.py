#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        count = nums.count(val)
        if not count:
            return len(nums)
        for i in range(count):
            nums.remove(val)
        return len(nums)

    def removeElement2(self, nums, val):
        if not nums:
            return 0
        last = 0
        for i, v in enumerate(nums):
            if v != val:
                nums[last] = nums[i]
                last += 1
        return last


if __name__ == '__main__':
    so = Solution()
    assert(so.removeElement([], 0) == 0)
    assert(so.removeElement([1], 0) == 1)
    assert(so.removeElement([1,2], 1) == 1)
    assert(so.removeElement([1,2], 2) == 1)
    assert(so.removeElement([1,1,2], 1) == 1)
    assert(so.removeElement([1,2,2,1], 1) == 2)
    assert(so.removeElement([0,1,2,2,3,0,4,2], 2) == 5)
