#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def combinationSum(self, candidates, target):
        if not candidates or target < 0:
            return []

        candidates.sort()
        total = len(candidates)

        ret = []

        def summary(target0, seq, last):
            if 0 == target0:
                ret.append(seq)
            for i in range(last, total):
                if candidates[i] <= target0:
                    summary(target0 - candidates[i], seq + [candidates[i]], i)  # [[..]]
                else:
                    break

        summary(target, [], 0)
        return ret


if __name__ == '__main__':
    so = Solution()


    def test(nums, t):
        print 'nums:', nums, ' target:', t, ' result:', so.combinationSum(nums, t)
        print


    test([2, 3, 6, 7, 1], 7)
    test([2, 3, 5], 8)
    test([2, 3], 1)
    test([], 1)
    test([5, 2, 9], 3)
    test([1], 1)
    test([1], 7)
    test([1, 2], 4)
    test([8, 7, 4, 3], 11)
