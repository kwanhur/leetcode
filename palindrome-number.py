#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            x_str = str(x)
            length = len(x_str)
            if length % 2 == 0:
                return int(x_str[:length / 2]) == int(x_str[length / 2:][::-1])
            else:
                return int(x_str[:length / 2]) == int(x_str[length / 2 + 1:][::-1])


if __name__ == '__main__':
    so = Solution()
    print so.isPalindrome(0)
    print so.isPalindrome(10)
    print so.isPalindrome(-200)
    print so.isPalindrome(101)
    print so.isPalindrome(110)
    print so.isPalindrome(1001)
    print so.isPalindrome(2008)
    print so.isPalindrome(1002)
    print so.isPalindrome(12321)
