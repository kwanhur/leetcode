#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def twoSum(self, nums, target):
        ret, seq = {}, {}
        for i in range(len(nums)):
            num = target - nums[i]
            if num in ret:
                seq[str(num) + "#" + str(nums[i])] = [num, nums[i]]
            else:
                ret[nums[i]] = i
        return seq.values()

    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []

        ret = []
        nums.sort()

        i, i_max = 0, len(nums) - 2
        while i < i_max and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            target = 0 - nums[i]
            p, q = i + 1, i_max + 1
            while p < q:
                s = nums[p] + nums[q]
                if s == target:
                    ret.append([nums[i], nums[p], nums[q]])
                    while p < q and nums[p] == nums[p + 1]:
                        p += 1
                    while p < q and nums[q] == nums[q - 1]:
                        q -= 1
                    p, q = p + 1, q - 1

                elif s < target:
                    p += 1
                else:
                    q -= 1

            i += 1
        return ret

    def threeSum3(self, nums):
        if not nums or len(nums) < 3:
            return []

        ret = []
        nums.sort()

        i, i_max = 0, len(nums) - 2
        while i < i_max and nums[i] <= 0:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            target = 0 - nums[i]
            seq = self.twoSum(nums[i + 1:], target)
            if seq:
                for s in seq:
                    s.append(nums[i])
                ret.extend(seq)
            i += 1
        return ret

    def threeSum2(self, nums):
        if not nums or len(nums) < 3:
            return []

        v_min, v_max = min(nums), max(nums)
        if v_min < 0 and v_max < 0:
            return []
        elif v_min > 0 and v_max > 0:
            return []

        ret = {}
        nums.sort()

        i, i_max = 0, len(nums) - 1
        while i < i_max - 1 and nums[i] <= 0:
            j = i + 1
            while j < i_max:
                if nums[i] == 0 and nums[j] == 0 and nums[j + 1] == 0:
                    n = 0
                    seq = [str(nums[i]), str(nums[j]), str(n)]
                    ret["#".join(seq)] = [nums[i], nums[j], n]
                    break

                n = -(nums[i] + nums[j])
                if n == nums[j]:
                    if nums[j:].count(n) >= 2:
                        seq = [str(nums[i]), str(nums[j]), str(n)]
                        ret["#".join(seq)] = [nums[i], nums[j], n]
                elif n in nums[j:]:
                    seq = [str(nums[i]), str(nums[j]), str(n)]
                    ret["#".join(seq)] = [nums[i], nums[j], n]
                j += 1
            i += 1
        return ret.values()


if __name__ == '__main__':
    so = Solution()
    assert (so.threeSum([]) == [])
    assert (so.threeSum([1, -1]) == [])
    assert (so.threeSum([1, 2, 3]) == [])
    assert (so.threeSum([-1, -2, -3]) == [])
    assert (so.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, 0, 1], [-1, -1, 2]])
    assert (so.threeSum([-1, 0, 1, 2, 1, -4]) == [[-1, 0, 1]])
    assert (so.threeSum([-1, 0, 0, 0, 1, 2, 1, -4]) == [[-1, 0, 1], [0, 0, 0]])
    assert (so.threeSum([0, 0, 0, 1, 2, 1]) == [[0, 0, 0]])
    assert (so.threeSum([-1, 0, 1, 0]) == [[-1, 0, 1]])
    assert (so.threeSum([0, 0, 0]) == [[0, 0, 0]])
    assert (so.threeSum([0, 0, 0, 0]) == [[0, 0, 0]])
    assert (so.threeSum([-2, -3, 0, 0, -2]) == [])
    assert (so.threeSum([-2, -3, 0, 0, 0]) == [[0, 0, 0]])
    assert (so.threeSum([1, 1, -2]) == [[-2, 1, 1]])
