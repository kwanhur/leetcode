#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def intToRoman(self, num):
        roman = {1: 'I',4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}

        if num <= 0:
            return ''

        ret = ''
        seq = roman.keys()
        seq.sort(reverse=True)
        for r in seq:
            if num >= r:
                c = num / r
                ret += roman[r] * c
                num -= r * c
        return ret


if __name__ == '__main__':
    so = Solution()
    #for i in range(1,4000):
    #    so.intToRoman(i)
    assert(so.intToRoman(0) == '')
    assert(so.intToRoman(1) == 'I')
    assert(so.intToRoman(4) == 'IV')
    assert(so.intToRoman(9) == 'IX')
    assert(so.intToRoman(58) == 'LVIII')
    assert(so.intToRoman(1994) == 'MCMXCIV')
    assert(so.intToRoman(2000) == 'MM')
    assert(so.intToRoman(3999) == 'MMMCMXCIX')
