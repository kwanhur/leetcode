#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        ret, seq = {}, []
        while head:
            v = head.val
            if v not in ret:
                ret[v] = head
                seq.append(v)
            head = head.next
        root = ListNode(0)
        head = root
        for i in seq:
            head.next = ret[i]
            head.next.next = None
            head = head.next
        return root.next

    def deleteDuplicates2(self, head):
        if not head:
            return
        root = ListNode(0)
        root.next = head
        last, head = head, head.next
        while head and head.next:
            if head.val != last.val:
                last.next = head
                last = last.next
            head = head.next
        if head and last.val == head.val:
            last.next = None
        elif head:
            last.next = head
        return root.next


def genList(l):
    root = ListNode(0)
    c = root
    for x in l:
        n = ListNode(x)
        c.next = n
        c = n
    return root.next


def printList(n):
    if not n:
        print "None"
        return
    s = ''
    while n:
        s += str(n.val) + '->'
        n = n.next
    print s[:-2]


if __name__ == '__main__':
    so = Solution()


    def test(l):
        l = genList(l)
        printList(l)
        l = so.deleteDuplicates(l)
        printList(l)


    test([1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7, 8, 9, 9])
    test([1])
    test([2, 2, 2, 2, 2])
    test([2, 2])
    test([1, 1, 1, 1, 4, 4, 4, 7, 5])
    test([1, 1, 2])
