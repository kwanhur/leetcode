#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return 0
        try:
            if nums[0] >= target:
                return 0
            if nums[-1] < target:
                return len(nums)
            return nums.index(target)
        except Exception:
            s, e = 0, len(nums)
            while True:
                position = (s + e) / 2
                if nums[position] == target:
                    return position
                elif nums[position] < target:
                    if len(nums[position:e + 1]) == 2:
                        return position + 1
                    else:
                        s = position
                        continue
                else:
                    if len(nums[s:position]) == 1:
                        return position
                    else:
                        e = position
                        continue


if __name__ == '__main__':
    so = Solution()
    assert(so.searchInsert([], 1) == 0)
    assert(so.searchInsert([0,1,2], 0) == 0)
    assert(so.searchInsert([0,1,2], -1) == 0)
    assert(so.searchInsert([0,1,2], 2) == 2)
    assert(so.searchInsert([0,1,2], 3) == 3)
    assert(so.searchInsert([0,1,2,3,4,5], 3) == 3)
    assert(so.searchInsert([0,1,2,4,5], 3) == 3)
    assert (so.searchInsert([0, 9, 20, 31, 45], 6) == 1)
    assert (so.searchInsert([0, 9, 20, 31, 45], 16) == 2)
    assert (so.searchInsert([0, 9, 20, 31, 45], 26) == 3)
    assert (so.searchInsert([0, 9, 20, 31, 45], 36) == 4)
