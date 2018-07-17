#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution(object):
    def isValid(self, s):
        if not s:
            return True 
        length = len(s)
        if length % 2 == 1:
            return False

        l = [''] * length
        last = -1
        for c in s:
            if c == '(' or c == '{' or c == '[':
                last += 1
                l[last] = c
                continue
            elif c == ')':
                if l[last] != '(':
                    return False
                l[last] = ''
            elif c == '}':
                if l[last] != '{':
                    return False
                l[last] = ''
            elif c == ']':
                if l[last] != '[':
                    return False
                l[last] = ''
            else:
                return False

            last -= 1

        return l[0] == ''


if __name__ == '__main__':
    so =Solution()
    assert(so.isValid("") == True) 
    assert(so.isValid("()") == True)
    assert(so.isValid("(}") == False)
    assert(so.isValid("()(){}") == True)
    assert(so.isValid("({[]})") == True)
    assert(so.isValid("({[}])") == False)
    assert(so.isValid("([)]") == False)
    assert(so.isValid("([[{((") == False)
    assert(so.isValid("[[{((") == False)
    assert(so.isValid("}]))]}")  == False)
    assert(so.isValid("(()(")  == False)
