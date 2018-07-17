#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    """
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
    """
    def lengthOfLongestSubstring(self, s):
        if not s:
            return 0

        b, l = 0, 0
        longest = -1
        length = len(s)

        subs = dict()
        while l < length:
            c = s[l]
            if c in subs and subs[c] >= b:
                b = subs[c] + 1
            tmp = l - b + 1
            if tmp > longest:
                longest = tmp

            subs[s[l]] = l
            l += 1
        return longest

    def lengthOfLongestSubstring3(self, s):
        if not s:
            return 0

        b, l = 0, 0
        longest = -1
        length = len(s)

        subs = set()
        while b < length and l < length:
            if s[l] not in subs:
                subs.add(s[l])
                l += 1
                if len(subs) > longest:
                    longest = len(subs)
            else:
                subs.remove(s[b])
                b += 1
        return longest
                
    def lengthOfLongestSubstring2(self, s):
        if not s:
            return 0

        subs = []
        longest = -1
        length = len(s)

        for i, c in enumerate(s):
            subs.append(c)
            for v in s[i+1:]:
                if v not in subs:
                    subs.append(v)
                else:
                    break
            if len(subs) > longest:
                longest = len(subs)
                if longest > length - i -1:
                    break
            subs = []
        return longest


if __name__ == '__main__':
    so = Solution()
    print so.lengthOfLongestSubstring("b")
    print so.lengthOfLongestSubstring("ba")
    print so.lengthOfLongestSubstring("bbbbbb")
    print so.lengthOfLongestSubstring("abcabc")
    print so.lengthOfLongestSubstring("pweektw")
    print so.lengthOfLongestSubstring("pwwkew")
    print so.lengthOfLongestSubstring("")
    print so.lengthOfLongestSubstring("kwanhur #$@")
    print so.lengthOfLongestSubstring("aab")
    print so.lengthOfLongestSubstring("abb")
    print so.lengthOfLongestSubstring("aabb")
