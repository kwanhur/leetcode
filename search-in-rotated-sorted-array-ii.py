#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def search(self, nums, target):
        """
        二分查找，需判断目标在左侧还是右侧
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            mid = (i + j) // 2
            if nums[mid] == target:
                return True

            if nums[i] < nums[mid]:
                if nums[i] <= target < nums[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            elif nums[i] > nums[mid]:
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid -1
            else:
                i = i + 1
        return False

    def search2(self, nums, target):
        """
        存在可重复 以某个支点旋转的数组
        """
        i, j = 0, len(nums) - 1
        while i <= j:
            if target == nums[i] or nums[j] == target:
                return True
            while i + 1 < j and nums[i] == nums[i + 1]:
                i += 1
            while i < j - 1 and nums[j] == nums[j - 1]:
                j -= 1

            i, j = i + 1, j - 1
        return False


if __name__ == '__main__':
    so = Solution()

    def test(n, t):
        print 'n:', n, ' target:', t, ' ret:', so.search(n, t)

    test([2,5,6,0,0,1,2], 3)
    test([1],1)
    test([2,5,6,0,0,1,2], 0)

