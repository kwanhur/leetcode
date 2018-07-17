#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def reverse(self, x):
        x_str = str(x)
        if x_str[0] == '-':
            ret = int('-' + x_str[1:][::-1])
            return ret if ret > -pow(2, 31) else 0
        else:
            ret = int(x_str[::-1])
            return ret if ret < pow(2, 31) - 1 else 0

    def reverse1(self, x):
        """
        正数结尾数字7 负数为8
        """
        max_v = (2**31 - 1) / 10
        min_v = (-2**31) / 10

        less = x < 0
        x_str = str(x)
        if less:
            x_str = x_str[1:]

        ret = 0
        i = len(x_str) - 1
        while i >= 0:
            v = int(x_str[i])
            
            if ret > max_v or (ret == max_v and v > 7):
                return 0
            if ret < min_v or (ret == min_v and v > -8):
                return 0
            ret = (ret * 10 + v) if not less else (ret * 10 - v)
            i -= 1
        return ret


    def reverse2(self, x):
        max_v = 2**31 - 1
        min_v = -2**31

        less = False
        if x >= 0:
            x_str = str(x)
        else:
            less = True
            x_str = str(x)
            x_str = x_str[1:]

        v_str = '' if not less else '-'
        i = len(x_str) - 1
        while i >= 0:
            v_str = v_str + x_str[i]
            i -= 1

        print 'x:', x, 'v:', v_str
        v_str = int(v_str)
        if v_str >=0:
            return v_str if v_str <= max_v else 0
        else:
            return v_str if v_str >= min_v else 0


if __name__ == '__main__':
    so = Solution()
    print so.reverse(0)
    print so.reverse(10)
    print so.reverse(299)
    print so.reverse(-222)
    print so.reverse(-1222)
    print so.reverse(-1563847412)
    print so.reverse(-9563847412)
    
