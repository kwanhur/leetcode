#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        增加一个头结点连接进行交换
        """
        root = p = ListNode(0)
        root.next = head
        while p.next and p.next.next:
            t = head
            p.next = head.next
            head.next = head.next.next
            p.next.next = t
            p = head
            head = head.next
        return root.next

    def swapPairs3(self, head):
        """
        根据是否存在两个进行交换
        """
        if not head or not head.next:
            return head

        root = p = ListNode(0)
        while head and head.next:
            t = head.next
            head.next = t.next
            t.next = head
            p.next = t
            p = head
            head = head.next
        return root.next

    def swapPairs2(self, head):
        p, q, t, i = head, head, None, 0
        while q:
            i, q = i + 1, q.next
            if i % 2 == 1:
                if q:
                    if t:
                        t.next, q = q, q.next
                        t.next.next, p = p, q
                        t, t.next = t.next.next, None
                    else:
                        t, q = q, q.next
                        t.next, p = p, q
                        t.next.next = None
                elif t:
                    t.next = p

                if t:
                    if i == 1:
                        head = t
                    if t.next:
                        t = t.next
            else:
                if q:
                    t.next, q = q, q.next
                    t.next.next, p = p, q
                    t, t.next = t.next.next, None
                else:
                    t.next = p

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
    l = genList([1, 2, 3, 4])
    l = so.swapPairs(l)
    printList(l)

    l = genList([1, 2, 3])
    l = so.swapPairs(l)
    printList(l)

    l = genList([1, 2, 3, 4, 5])
    l = so.swapPairs(l)
    printList(l)

    l = genList([1, 2, 3, 4, 5, 6])
    l = so.swapPairs(l)
    printList(l)

    l = genList([1])
    l = so.swapPairs(l)
    printList(l)

    l = genList([1, 2])
    l = so.swapPairs(l)
    printList(l)

    l = genList([2, 5, 3, 4, 6, 2, 2])
    l = so.swapPairs(l)
    printList(l)
