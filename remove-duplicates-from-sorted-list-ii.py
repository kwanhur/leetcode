#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return

        root = ListNode(0)
        node = root

        while head:
            dup, h = False, head.next
            while h:
                if h.val == head.val:
                    dup, h = True, h.next
                else:
                    break
            if not dup:
                node.next = head
                head, node = head.next, node.next
                node.next = None
            else:
                head = h
        return root.next

    def deleteDuplicates2(self, head):
        if not head:
            return

        root = ListNode(0)
        node, count = root, 0

        while head:
            count += 1
            if not head.next and count == 1:
                node.next, head = head, head.next

            elif head.next and head.val != head.next.val:
                if count == 1:
                    node.next, head = head, head.next
                    node.next.next, node = None, node.next
                else:
                    head = head.next
                count = 0
            else:
                head = head.next

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
