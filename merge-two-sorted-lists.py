#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1

        root = ListNode(-1)
        c = root
        while True:
            if l1 and l2:
                if l1.val == l2.val:
                    t1, t2 = l1, l2
                    l1, l2 = l1.next, l2.next
                    c.next, c = t1, t1
                    c.next, c = t2, t2
                elif l1.val < l2.val:
                    t,l1 = l1, l1.next
                    c.next, c = t, t
                elif l1.val > l2.val:
                    t, l2 = l2, l2.next
                    c.next, c = t, t
            elif not l1:
                c.next = l2
                break
            elif not l2:
                c.next = l1
                break
        return root.next


def genList(l):
    l.sort()
    root = ListNode(0)
    c = root
    for x in l:
        n = ListNode(x)
        c.next = n
        c = n
    return root.next


def printList(n):
    if not n:
        print ""
        return
    s = ''
    while n:
        s += str(n.val) + '->'
        n = n.next
    print s[:-2]


if __name__ == '__main__':
    so = Solution()
    l1 = genList([1,2,4])
    l2 = genList([1,3,4])
    printList(so.mergeTwoLists(l1, l2))
    l1 = genList([1, 4, 9, 11, 13])
    l2 = genList([1, 3, 4])
    printList(so.mergeTwoLists(l1, l2))
    l1 = genList([2,4,9,11])
    l2 = genList([1,3,4])
    printList(so.mergeTwoLists(l1, l2))
    l1 = genList([])
    l2 = genList([])
    printList(so.mergeTwoLists(l1, l2))
    l1 = genList([])
    l2 = genList([1,3,4])
    printList(so.mergeTwoLists(l1, l2))
    l1 = genList([2,3,4])
    l2 = genList([6,7,8,9,10])
    printList(so.mergeTwoLists(l1, l2))
