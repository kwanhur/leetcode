#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def maxArea(self, height):
        if not height or len(height) < 2:
            return 0
        
        i, j = 0, len(height) - 1
        ret = 0
        while i < j:
            ret = max(ret, (j - i) * min([height[i], height[j]]))
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1
        return ret

    def maxArea2(self, height):
        if not height or len(height) < 2:
            return 0

        ret = 0
        h = [i for i in range(len(height))]
        for i in h:
            for j in h[i + 1:]:
                ret = max(ret, (j - i) * min([height[i], height[j]]))
        return ret


if __name__ == '__main__':
    so = Solution()
    assert(so.maxArea([10, 5]) == 5)
    assert(so.maxArea([10, 5]) == so.maxArea2([10, 5]))
