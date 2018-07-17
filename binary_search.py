#! /usr/bin/env python
# _*_ coding:utf-8 _*_


def search(l, n):
    if not l:
        return False
    if len(l) == 1:
        return l[0] == n

    while 1:
        mid = len(l) / 2
        mid_n = l[mid]

        if mid == 0:
            return mid_n == n

        if mid_n > n:
            l = l[:mid]
            continue
        if mid_n < n:
            l = l[mid:]
            continue
        return mid_n == n


if __name__ == '__main__':
    l = [1, 3, 5, 2, 7, 0, 3]
    l.sort()
    print len(l)
    print l
    print search(l, 3)
    print search(l, 9)
