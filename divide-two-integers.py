#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def divide(self, dividend, divisor):
        """
        位运算 异或 左移 右移
        """
        if not divisor:
            return
        if not dividend:
            return dividend

        less1 = True if dividend < 0 else False
        less2 = True if divisor < 0 else False
        less3 = True if (less1 and not less2) or (not less1 and less2) else False
        dividend = dividend if not less1 else -dividend
        divisor = divisor if not less2 else -divisor

        ret = 0
        if divisor == 1:
            ret = dividend
        elif divisor == 2:
            ret = dividend >> 1
        else:
            while dividend >= divisor:
                n, c = divisor, 1
                while dividend >= (n << 1):
                    n <<= 1  # divisor * 2
                    c <<= 1
                dividend -= n
                ret += c

        i_max, i_min = (2 << 30) - 1, -2 << 30
        ret = ret if not less3 else -ret
        if ret > i_max or ret < i_min:
            return i_max

        return ret


if __name__ == '__main__':
    so = Solution()
    assert (so.divide(0, -1) == 0)
    assert (so.divide(1, 1) == 1)
    assert (so.divide(10, 3) == 3)
    assert (so.divide(7, -3) == -2)
    assert (so.divide(-7, 3) == -2)
    assert (so.divide(-10, -3) == 3)
    assert (so.divide(-3, 7) == 0)
    assert (so.divide(3, 7) == 0)
    assert (so.divide(127, -128) == 0)
    assert (so.divide(-128, 127) == -1)
    assert (so.divide(-2 ** 31, 2 ** 31 - 1) == -1)
    assert (so.divide(2 ** 31 - 1, -2 ** 31) == 0)
    assert (so.divide(2 ** 31 - 1, -1) == -2 ** 31 + 1)
    assert (so.divide(2 ** 31 - 1, 1) == 2 ** 31 - 1)
    assert (so.divide(-2 ** 31, -1) == 2 ** 31 - 1)
    assert (so.divide(-2 ** 31, 1) == -2 ** 31)

    assert (so.divide(2 ** 31 - 1, 2) == 2 ** 30 - 1)
    assert (so.divide(2 ** 31 - 1, 3) == 715827882)
