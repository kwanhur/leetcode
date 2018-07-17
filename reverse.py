#! /usr/bin/env python
# _*_ coding:utf-8 _*_


def revert(str):
    if not str or len(str) == 1:
        return str

    i, base, s = -1, -len(str), ''
    while True:
        s += str[i]
        i -= 1
        if i < base:
            break
    return s


def revert_iterator(str):
    s = ''
    if not str or len(str) == 1:
        return str or s
    else:
        s = str[-1] + revert_iterator(str[0:len(str) - 1])
    return s


if __name__ == '__main__':
    s = "string"
    print s[::-1]
    print revert(s)
    print revert_iterator(s)
