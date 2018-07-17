#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        pre = None
        for s in strs:
            if pre is None:
                pre = s
            else:
                j = len(pre) if len(pre) < len(s) else len(s)
                pre = pre[:j]
                for i in range(j):
                    if pre[i] != s[i]:
                        pre = pre[:i]
                        break
                if pre == "":
                    break
        return pre

    def longestCommonPrefix2(self, strs):
        if not strs:
            return ""

        diff = False
        i = 0

        while True:
            c = None
            for s in strs:
                if i >= len(s):
                    diff = True
                    break
                if c == None:
                    c = s[i]
                elif c != s[i]:
                    diff = True
                    break
                else:
                    diff = False
            if diff:
                break
            i += 1

        return strs[0][: i]


if __name__ == '__main__':
    so = Solution()
    l1 = ["flower","flow","flight"]
    print so.longestCommonPrefix(l1)
    l1 = ["dog","racecar","car"]
    print so.longestCommonPrefix(l1)
    l1 = ["dog"]
    print so.longestCommonPrefix(l1)
    l1 = ["aa","a"]
    print so.longestCommonPrefix(l1)

