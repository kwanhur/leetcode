#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def combinationSum2(self, candidates, target):
        if not candidates or target <= 0:
            return []

        candidates.sort()
        total = len(candidates)
        ret = {}

        def summary(target0, seq, start):
            if 0 == target0:
                ret[str(seq)] = seq
                return

            i = start
            while i < total:
                if i != start and candidates[i] == candidates[start]:
                    i += 1
                    continue
                else:
                    if candidates[i] <= target0:
                        summary(target0 - candidates[i], seq + [candidates[i]], i + 1)
                        while i + 1 < total and candidates[i] == candidates[i + 1]:
                            i += 1
                        i += 1
                    else:
                        break

        summary(target, [], 0)
        return ret.values()


if __name__ == '__main__':
    so = Solution()


    def test(nums, t):
        print 'nums:', nums, ' t:', t, ' ret:', so.combinationSum2(nums, t)


    test([10, 1, 2, 7, 6, 1, 5], 8)
    test([2, 5, 2, 1, 2], 5)
    test([2, 3, 6, 7, 1], 7)
    test([2, 3, 5], 8)
    test([2, 3], 1)
    test([], 1)
    test([5, 2, 9], 3)
    test([1, 1], 1)
    test([1], 1)
    test([1], 7)
    test([1, 2], 4)
    test([8, 7, 4, 3], 11)
    test([1, 1, 1, 3, 3, 5], 8)
    test([1, 1, 1, 3, 3, 5], 5)
