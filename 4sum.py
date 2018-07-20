#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def fourSum(self, nums, target):
        if not nums or len(nums) < 4:
            return []

        ret = {}
        nums.sort()

        i, i_max = 0, len(nums) - 3
        while i < i_max:
            three_target = target - nums[i]
            j, j_max = i + 1, i_max + 1
            while j < j_max:
                two_target = three_target - nums[j]
                p, q = j + 1, j_max + 1
                while p < q:
                    s = nums[p] + nums[q]
                    if s == two_target:
                        ret["#".join([str(nums[i]), str(nums[j]), str(nums[p]), str(nums[q])])] = [nums[i], nums[j],
                                                                                                   nums[p], nums[q]]
                        while p < q and nums[p] == nums[p + 1]:
                            p += 1
                        while p < q and nums[q] == nums[q - 1]:
                            q -= 1
                        p, q = p + 1, q - 1
                    elif s < two_target:
                        p += 1
                    else:
                        q -= 1
                j += 1
            i += 1
        return ret.values()


if __name__ == '__main__':
    so = Solution()
    print so.fourSum([1, 0, -1, 0, -2, 2], 0)
    print so.fourSum([0, 0, 0, 0], 0)
    print so.fourSum([0, 0, 0, 0, 1, 1, -1, -1], 0)
    print so.fourSum([1, -2, -5, -4, -3, 3, 3, 5], -11)
