#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def getPalindrome(self, s, i, j):
        while i >=0 and j < len(s):
            if s[i] == s[j]:
                i, j = i - 1, j + 1
            else:
                break
        return s[i + 1: j]

    def longestPalindrome(self, s):
        if not s or len(s) == 1:
            return s
        
        pal = ""
        for i in range(len(s)):
            tmp = self.getPalindrome(s, i, i)
            if len(tmp) > len(pal):
                pal = tmp
            tmp = self.getPalindrome(s, i, i + 1)
            if len(tmp) > len(pal):
                pal = tmp

        return pal


if __name__ == '__main__':
    so = Solution()
    assert(so.longestPalindrome("") == "")
    assert(so.longestPalindrome("a") == "a")
    assert(so.longestPalindrome("aa") == "aa")
    assert(so.longestPalindrome("ab") == "a")
    assert(so.longestPalindrome("abc") == "a")
    assert(so.longestPalindrome("aba") == "aba")
    assert(so.longestPalindrome("abab") == "aba")
    assert(so.longestPalindrome("cbba") == "bb")
