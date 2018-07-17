#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    """
    https://leetcode-cn.com/problems/add-two-numbers/
    """
    def add_next(self, l):
        last = l
        extra = 1
        while True:
            val = l.val + extra
            if val >= 10:
                val = val - 10
                extra = 1
            else:
                extra = 0
            l.val = val
            if extra == 0:
                if not l.next:
                    break
                else:
                    l = l.next
            elif not l.next:
                n = ListNode(1)
                l.next = n
                break
            else:
                l = l.next

        return last

    def addTwoNumbers(self, l1, l2):
        l3 = ListNode(0)
        last = l3
        extra = 0

        while l1 or l2 :
            val1 = 0 if not l1 else l1.val
            val2 = 0 if not l2 else l2.val
            val = val1 + val2 + extra
            if val >= 10:
                val = val - 10
                extra = 1
            else:
                extra = 0
            last.next = ListNode(val)
            last = last.next

            l1 = None if not l1 else l1.next
            l2 = None if not l2 else l2.next

        if extra == 1:
            last.next = ListNode(1)
        return l3.next

    def addTwoNumbers2(self, l1, l2):
        l3 = ListNode(0)
        last = l3
        extra = 0
        while True:
            val = l1.val + l2.val + extra
            if val >= 10:
                val = val - 10
                extra = 1
            else:
                extra = 0
            n = ListNode(val)
            last.next = n
            last = n

            if not l1.next and l2.next:
                if extra == 1:
                    last.next = self.add_next(l2.next)
                else:
                    last.next = l2.next
                break

            if l1.next and not l2.next:
                if extra == 1:
                    last.next = self.add_next(l1.next)
                else:
                    last.next = l1.next
                break

            if not l1.next and not l2.next:
                if extra == 1:
                    n = ListNode(1)
                    last.next = n
                    last = n
                break

            l1 = l1.next
            l2 = l2.next

        return l3.next


def gen_node(nums):
    l = ListNode(nums[0])
    last = l
    for i in nums[1:]:
        n = ListNode(i)
        last.next = n
        last = n
    return l


def output_node(n):
    str1 = ''
    while True:
        str1 = str1 + str(n.val)
        if not n.next:
            break
        n = n.next
        str1 = str1 + '->'
    print str1


if __name__ == '__main__':
    n1 = [2, 4, 3]
    n2 = [5, 6, 4]
    l1 = gen_node(n1)
    output_node(l1)
    l2 = gen_node(n2)
    output_node(l2)
    so = Solution()
    l3 = so.addTwoNumbers(l1, l2)
    output_node(l3)

    l1 = gen_node([6])
    l2 = gen_node([5])
    l3 = so.addTwoNumbers(l1, l2)
    output_node(l3)

    l1 = gen_node([6,9])
    l2 = gen_node([5])
    l3 = so.addTwoNumbers(l1, l2)
    output_node(l3)

