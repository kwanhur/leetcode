#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        last = 0
        for i, v in enumerate(nums):
            if nums[i] != nums[last]:
                last += 1
                nums[last] = nums[i]
        return last + 1


if __name__ == '__main__':
    so = Solution()
    assert(so.removeDuplicates([1,1,2]) == 2)
    assert(so.removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5)
    assert(so.removeDuplicates([0,4]) == 2)
    assert(so.removeDuplicates([]) == 0)
    assert(so.removeDuplicates([1]) == 1)
    assert(so.removeDuplicates([1,2,3,4,5]) == 5)
