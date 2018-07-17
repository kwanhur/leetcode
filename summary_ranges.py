#! /usr/bin/env python
# _*_ coding:utf-8 _*_
__author__ = 'kwanhur'


class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        result = []
        start_index, end_index = 0, 0
        for index, num in enumerate(nums):
            if index + 1 < len(nums):
                if nums[index + 1] - num == 1:
                    end_index += 1
                    continue
                else:
                    if start_index == end_index:
                        result.append("{0}".format(nums[start_index]))
                    else:
                        result.append("{0}->{1}".format(*(nums[start_index], nums[end_index])))
                    start_index = end_index = index + 1
            else:
                if start_index == end_index == index:
                    result.append('{0}'.format(nums[index]))
                else:
                    result.append("{0}->{1}".format(*(nums[start_index], nums[index])))
        return result


if __name__ == '__main__':
    solution = Solution()
    ar = solution.summaryRanges([0, 1, 2, 8, 10, 16])
    print(ar)