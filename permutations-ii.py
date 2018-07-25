#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def permuteUnique(self, nums):
        if not nums:
            return nums
        nums.sort()

        def arrange(nums0, total):
            if total == 1:
                return [nums0]

            ret, i = [], 0
            while i < total:
                res = arrange(nums0[:i] + nums0[i + 1:], total - 1)
                v = [nums0[i]]
                for item in res:
                    ret.append(v + item)
                while i + 1 < total and nums0[i] == nums0[i + 1]:
                    i += 1
                i += 1
            return ret

        return arrange(nums, len(nums))


if __name__ == '__main__':
    so = Solution()

    def test(nums):
        print 'nums:', nums, ' ret:\n', so.permuteUnique(nums)

    test([1,1,2])
    test([1,1,2,2,3])
    test([1])
    test([1,1,1,1,3,3,3,3,5,5,5,6,6,6,7,7,7,8])
