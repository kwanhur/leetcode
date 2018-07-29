#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def canJump(self, nums):
        if not nums or nums.count(0) == 0:
            return True

        for idx, n in enumerate(nums):
            if n > 0:
                continue

            can = False
            for i in range(idx - 1, -1, -1):
                if idx - i < nums[i]:
                    can = True
            if not can:
                if idx == len(nums) - 1:
                    return True
                return False
        return True

    def canJump2(self, nums):
        if not nums:
            return True

        def jump(idx):
            n, remain = nums[idx], len(nums) - idx - 1
            if n >= remain:
                return True
            while n > 0:
                # for i in range(1, n + 1):
                if remain - n <= 0:
                    return True
                elif jump(idx + n):
                    return True
                n -= 1
            return False

        return jump(0)


if __name__ == '__main__':
    so = Solution()


    def test(nums):
        print 'nums:', nums, ' can:', so.canJump(nums)


    # test([2, 3, 1, 1, 4])
    # test([3, 2, 1, 0, 4])
    test([0])
    test([1])
    test([1, 0])
    test([0, 1, 2])
    test([2, 1, 0, 3, 1])
    test([3, 1, 0, 3, 1])
    test([1, 2, 1, 0, 1])
    test([1, 3, 1, 0, 1])
