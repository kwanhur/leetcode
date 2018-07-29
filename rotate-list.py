#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        形成环，计算需走步数确定尾节点，重置头节点
        """
        if not head or k <= 0:
            return head

        tail, total = head, 0
        while True:
            total += 1
            if not tail.next:
                tail.next, tail = head, head
                break
            tail = tail.next

        n = total - k % total - 1
        while n > 0:
            tail = tail.next
            n -= 1
        head, tail.next = tail.next, None

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

    def test(l, k):
        l = genList(l)
        print 'k:', k, 'origin:'
        printList(l)
        print 'ret:'
        printList(so.rotateRight(l, k))


    test([1,2,3,4,5], 0)
    test([1,2,3,4,5], 1)
    test([1,2,3,4,5], 2)
    test([1,2,3,4,5], 3)
    test([1,2,3,4,5], 4)
    test([1,2,3,4,5], 5)
    test([1],1)
    test([1],2)
    test([1],3)
    test([1],4)
