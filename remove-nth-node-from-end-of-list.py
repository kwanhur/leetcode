#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head or not n:
            return head

        i, p, q = 0, head, head
        if n < 0:
            while i < -n and p:
                i += 1
                if i == -n and p.next:
                    p.next = p.next.next
                p = p.next
            return p
        else:
            for i in range(n):
                if q:
                    q = q.next
                else:
                    return head

            while q:
                if q.next:
                    p, q = p.next, q.next
                else:
                    p.next = p.next.next
                    return head
            else:
                t = p.next
                if t:
                    p = t
                else:
                    p = q
                return p

    def removeNthFromEnd2(self, head, n):
        if not head or not n:
            return head

        i, l = 0, head
        while l:
            i += 1
            l = l.next

        n1 = i - n if n > 0 else i + n
        if n1 == 0:
            return head.next
        elif n1 < 0:
            return head

        i, l = 0, head
        while l:
            if n1 - 1 == i:
                l.next = l.next.next
                break
            l = l.next
            i += 1
        return head


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
    l = genList([1])
    l = so.removeNthFromEnd(l, 1)
    printList(l)

    l = genList([1, 2, 3, 4, 5, 6])
    printList(l)

    l = so.removeNthFromEnd(l, 7)
    printList(l)

    l = so.removeNthFromEnd(l, 1)
    printList(l)

    l = so.removeNthFromEnd(l, 5)
    printList(l)

    l = so.removeNthFromEnd(l, -1)
    printList(l)
