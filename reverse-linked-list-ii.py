#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        if not head:
            return

        mprev, nnext = None, None
        node, i, mnlist = head, 1, []
        while node:
            if i < m:
                mprev = node
            elif m <= i <= n:
                mnlist.append(node)

            if i == n:
                nnext, mncount = node.next, len(mnlist)
                for j in range(-1, -mncount - 1, -1):
                    if j == -1:
                        if mprev:
                            mprev.next = mnlist[j]
                        else:
                            head = mnlist[j]
                    if j == -mncount:
                        mnlist[j].next = nnext
                        break
                    mnlist[j].next = mnlist[j - 1]

                break
            i += 1
            node = node.next

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


    def test(l, m, n):
        l = genList(l)
        print 'ori:'
        printList(l)
        print 'ret:'
        l = so.reverseBetween(l, m, n)
        printList(l)


    test([1, 2, 3, 4, 5, 6, 7], 2, 5)
    test([1], 1, 1)
    test([1, 2, 3], 1, 3)
    test([1, 2, 3, 4, 5], 5, 5)
    test([1, 2, 3, 4, 5], 4, 5)
    test([1, 2, 3, 4], 1, 1)
    test([1, 2, 3, 4, 5], 2, 2)
