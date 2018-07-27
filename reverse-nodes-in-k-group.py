#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        first group then reverse
        """
        if not head or k <= 1:
            return head

        i, root = 0, ListNode(0)
        last = root
        while True:
            if i % k == 0:
                ele = []
            if head:
                ele.append(head)
                head = head.next
                if i % k == k - 1:
                    for j in range(-1, -k - 1, -1):
                        last.next = ele[j]
                        last = last.next
                        last.next = None
            else:
                if len(ele) > 0:
                    last.next = ele[0]
                break
            i += 1

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
        print "NoneNone"
        return
    s = ''
    while n:
        s += str(n.val) + '->'
        n = n.next
    print s[:-2]


if __name__ == '__main__':
    so = Solution()


    def test(l, k):
        print 'k,', k, 'origin:'
        printList(l)
        print 'ret:'
        printList(so.reverseKGroup(l, k))


    l = genList([1, 2])
    test(l, 3)
    l = genList([1])
    test(l, 3)
    l = genList([])
    test(l, 3)
    l = genList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    test(l, 1)
    l = genList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    test(l, 2)
    l = genList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    test(l, 3)
    l = genList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    test(l, 4)
    l = genList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    test(l, 5)
    l = genList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
    test(l, 6)
    l = genList([1, 2])
    test(l, 2)
