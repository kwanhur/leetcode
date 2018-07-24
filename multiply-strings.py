#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def multiply(self, num1, num2):
        return str(int(num1) * int(num2))

    def multiply2(self, num1, num2):
        l1, l2 = len(num1), len(num2)
        if not l1 or not l2:
            return
        if num1[0] == '0' or num2[0] == 0:
            return '0'
        elif l1 == 1 and num1[0] == '1':
            return num2
        elif l2 == 1 and num2[0] == '1':
            return num1

        n1 = map(lambda v: ord(v) - 48, num1)
        n1 = reduce(lambda x, y:  x * 10 + y, n1)
        n2 = map(lambda v: ord(v) - 48, num2)
        n2 = reduce(lambda x, y:  x * 10 + y, n2)
        return str(n1 * n2)


if __name__ == '__main__':
    so = Solution()
    assert so.multiply('11', '11') == '121'
    assert so.multiply('0', '11') == '0'
    assert so.multiply('0', '0') == '0'
    assert so.multiply('123', '456') == '56088'
    assert so.multiply('99999', '1') == '99999'
    so.multiply('9' * 109, '1' * 109)
