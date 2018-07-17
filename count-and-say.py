#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def countAndSay(self, n):
        if n <= 0:
            return ''
        if n == 1:
            return '1'

        s = self.countAndSay(n - 1)
        num = 1
        ret, length = '', len(s)
        for i in range(length):
            if i != length - 1 and s[i] == s[i + 1]:
                num += 1
            else:
                ret += str(num) + s[i]
                num = 1
        return ret

    def countAndSay2(self, n):
        s = ''
        if n <= 0:
            return s
        if n == 1:
            return '1'

        s += self.countAndSay(n - 1)
        c, num = None, 0 
        ret, length = '', len(s)
        for i, v in enumerate(s): 
            if c == None:
                c, num = v, 1
            elif c == v:
                num += 1
            else:
                ret += str(num) + c
                c, num = v, 1
            if i + 1 == length:
                ret += str(num) + c
        return ret


if __name__ == '__main__':
    so = Solution()
    assert(so.countAndSay(0) == '')
    assert(so.countAndSay(1) == '1')
    assert(so.countAndSay(2) == '11')
    assert(so.countAndSay(3) == '21')
    assert(so.countAndSay(4) == '1211')
    assert(so.countAndSay(5) == '111221')
    assert(so.countAndSay(6) == '312211')
