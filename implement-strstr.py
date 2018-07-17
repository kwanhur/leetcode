#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def strStr(self, haystack, needle):
        return haystack.find(needle)

    def strStr2(self, haystack, needle):
        if not haystack and not needle:
            return 0
        if not haystack and needle:
            return -1
        try:
            return haystack.index(needle)
        except Exception:
            return -1


if __name__ == '__main__':
    so = Solution()
    assert(so.strStr("", "") == 0)
    assert(so.strStr("", "kw") == -1)
    assert(so.strStr("kwanhur", "") == 0)
    assert(so.strStr("kwanhur", "kw") == 0)
    assert(so.strStr("kwanhur", "hur") == 4)
    assert(so.strStr("kwanhur", "hua") == -1)
