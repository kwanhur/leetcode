#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def romanToInt(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rule = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
        if not s:
            return 0
        if len(s) == 1:
            return roman[s]
        
        ret, length = 0, len(s)
        i = 0
        while i < length:
            c = s[i]
            if i + 1 < length:
                d = s[i + 1]
                if d != 'I' and c == rule[d]:
                    ret += roman[d] - roman[c]
                    i += 2
                    continue

            ret += roman[c]
            i += 1
        return ret

    def romanToInt2(self, s):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rule = {'I': ['V', 'X'], 'X': ['L', 'C'], 'C':['D', 'M']}
        rules = rule.keys()
        if not s:
            return 0
        if len(s) == 1:
            return roman[s]
        
        ret, length = 0, len(s)
        i = 0
        while i < length:
            c = s[i]
            if i + 1 < length:
                if c in rules and s[i + 1] in rule[c]:
                    ret +=  roman[s[i + 1]] - roman[c]
                    i += 2
                    continue

            ret += roman[c]
            i += 1
        return ret


if __name__ == '__main__':
    so = Solution()
    print so.romanToInt('III')
    print so.romanToInt('IV')
    print so.romanToInt('LVIII')
    print so.romanToInt('MCMXCIV')
