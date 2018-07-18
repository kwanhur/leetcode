#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def myAtoi(self, str):
        s = str
        str = str.strip()
        if not str or (str[0] != '-' and str[0] != '+' and not str[0].isdigit()):
            return 0

        INT_MAX, INT_MIN = (2 << 30) - 1, -2 << 30

        index = str.find(' ')
        if index > 0:
            str = str[0: index]
            
        unsinged = True
        if not str[0].isdigit():
            unsinged = str[0] == '+'
            str = str[1:]
        ret = 0
        for index, val in enumerate(str):
            if not val.isdigit():
                break
            else:
                ret = ret * 10 + int(val)
        if not unsinged:
            ret = -ret
        return ret if ret >= INT_MIN and ret <= INT_MAX else INT_MAX if ret > INT_MAX else INT_MIN



if __name__ == '__main__':
    so = Solution()
    assert(so.myAtoi("word 987") == 0)
    assert(so.myAtoi("   ") == 0)
    assert(so.myAtoi("   -42") == -42)
    assert(so.myAtoi("4193 with word") == 4193)
    assert(so.myAtoi("-4193 with word") == -4193)
    assert(so.myAtoi("-91283472332") == -2<<30)
    assert(so.myAtoi("91283472332") == (2<<30) - 1)
    assert(so.myAtoi("+kwan987") == 0)
    assert(so.myAtoi("-kwan987") == 0)
    assert(so.myAtoi("+987") == 987)
    assert(so.myAtoi("-987") == -987)
    assert(so.myAtoi("+91283472332") == (2<<30)-1)
    assert(so.myAtoi("+9128kwan") == 9128)
    assert(so.myAtoi("-9128kwan") == -9128)

