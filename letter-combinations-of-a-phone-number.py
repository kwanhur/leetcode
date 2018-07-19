#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def letterCombinations(self, digits):
        num = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        ret = []
        if not digits or len(digits) == 1:
            return num.get(digits, [])

        cs = num.get(digits[0])
        res = self.letterCombinations(digits[1:])
        if not cs:
            ret = res
        elif res:
            four = len(cs) == 4
            for v in res:
                ret.append(cs[0] + v)
                ret.append(cs[1] + v)
                ret.append(cs[2] + v)
                if four:
                    ret.append(cs[3] + v)

        return ret


if __name__ == '__main__':
    so = Solution()
    print so.letterCombinations("")
    print so.letterCombinations("23")
    print so.letterCombinations("345")
    print so.letterCombinations("264")
    print so.letterCombinations("875")
