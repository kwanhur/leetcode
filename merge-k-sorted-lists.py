#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return

        ret = []
        for l in lists:
            while l:
                ret.append(l.val)
                l = l.next
        ret.sort()
        root = ListNode(0)
        n = root
        for i in ret:
            n1 = ListNode(i)
            n.next = n1
            n = n1
        return root.next

    def mergeKLists2(self, lists):
        if not lists: 
            return None

        root = ListNode(0)
        last = root

        for l in lists:
            if not last.next:
                last.next = l
            else:
                if l and last is not root and last.val < l.val:
                    last = root
                while l:
                    if last.next and last.next.val >= l.val:
                        t, l = l, l.next
                        t.next = last.next
                        last.next = t
                    else:
                        if not last.next:
                            last.next = l
                            break
                        else:
                            last = last.next
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


    def test(l):
        n = so.mergeKLists(l)
        printList(n)


    test([genList([1, 4, 5]), genList([1, 3, 4]), genList([2, 6])])
    test([genList([]), genList([1, 3, 4]), genList([])])
    test([genList([1, 4, 5]), genList([]), genList([6])])
    test([genList([]), genList([]), genList([])])
    test([genList([])])
    test([genList([5])])
