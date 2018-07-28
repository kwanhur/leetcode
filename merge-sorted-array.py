#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, 0
        while j < n:
            nums1[i] = nums2[j]
            i, j = i + 1, j + 1
        nums1.sort()

        # nums1[m:] = nums2[:n]


if __name__ == '__main__':
    so = Solution()

    def test():
        pass

    test()

