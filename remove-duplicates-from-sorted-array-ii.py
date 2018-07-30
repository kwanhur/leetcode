#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        last, count, j = None, 0, 0
        for n in nums:
            if n != last:
                last, count = n, 1
            else:
                count += 1
            if count <= 2:
                nums[j], j = n, j + 1
        return j

    def removeDuplicates2(self, nums):
        """
        允许单个元素可重复2次
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        last, c = 0, 0
        for i, v in enumerate(nums):
            if nums[i] != nums[last]:
                print 'last:', last, ' i:', i, ' c:', c
                last, c = i, 1
            else:
                c += 1
                if c > 2:
                    nums[i] = None
                    print 'last:', last
                else:
                    last = i
        print nums

        return len(nums)


if __name__ == '__main__':
    so = Solution()
    # assert (so.removeDuplicates([1, 1, 2]) == 3)
    # assert (so.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 9)
    # assert (so.removeDuplicates([0, 4]) == 2)
    # assert (so.removeDuplicates([]) == 0)
    # assert (so.removeDuplicates([1]) == 1)
    # assert (so.removeDuplicates([1, 2, 3, 4, 5]) == 5)
    so.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
