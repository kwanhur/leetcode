#! /usr/bin/env 
# _*_ coding:utf-8 _*_


class Solution(object):
    def threeSumClosest(self, nums, target):
        if not nums or len(nums) < 3:
            return 0

        nums.sort()
        i, i_max = 0, len(nums) - 2

        ret = nums[0] + nums[1] + nums[2]
        while i < i_max:
            if nums[i] == nums[i - 1]:
                i += 1
                continue
            p, q = i + 1, i_max + 1
            while p < q:
                sum1 = nums[i] + nums[p] + nums[q]
                if sum1 == target:
                    return sum1
                elif abs(target - sum1) < abs(target - ret):
                    ret = sum1

                if sum1 <= target:
                    p += 1
                else:
                    q -= 1
            i += 1
        return ret

    def threeSumClosest2(self, nums, target):
        if not nums or len(nums) < 3:
            return 0

        i, i_max = 0, len(nums) - 2

        ret, last = None, None
        while i < i_max:
            target1 = nums[i] - target
            p = i + 1
            while p < i_max + 1:
                target2 = target1 + nums[p]
                q = p + 1
                while q < i_max + 2:
                    sum1 = target2 + nums[q]
                    t1 = sum1 if sum1 >= 0 else -sum1
                    if sum1 == 0:
                        return sum1 + target
                    if last and t1 < last or not last:
                        last, ret = t1, sum1 + target

                    q += 1

                p += 1

            i += 1

        return ret


if __name__ == '__main__':
    so = Solution()
    assert (so.threeSumClosest([1, 1, -1, -1, 3], -1) == -1)
    assert (so.threeSumClosest([0, 2, 1, -3], 1) == 0)
    assert (so.threeSumClosest([-1, 0, 1, -2], 1) == 0)
    assert (so.threeSumClosest([-1, 2, 1, -4], 1) == 2)
    assert (so.threeSumClosest([0, 0, 0], 1) == 0)
    assert (so.threeSumClosest([1, 1, 1], 1) == 3)
    assert (so.threeSumClosest([1, 0, -1], 1) == 0)
    assert (so.threeSumClosest([-2, -4, -9, 3, 5, 8, 21], 10) == 10)
