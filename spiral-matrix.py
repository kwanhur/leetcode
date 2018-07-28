#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def spiralOrder(self, matrix):
        ret = []
        if not matrix:
            return ret

        while matrix:
            row = matrix.pop(0)
            ret.extend(row)
            if matrix:
                row = map(lambda x: x and x.pop(-1), matrix)
                ret.extend(row)
            matrix = filter(lambda x: x, matrix)
            if matrix:
                row = matrix.pop(-1)
                row = row[::-1]
                ret.extend(row)
            matrix = filter(lambda x: x, matrix)
            if matrix:
                row = map(lambda x: x and x.pop(0), matrix)
                row = row[::-1]
                ret.extend(row)
        return ret


if __name__ == '__main__':
    so = Solution()

    def test(n):
        print "n:"
        print n
        print "ret:"
        print so.spiralOrder(n)

    test([
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ])

    test([
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ])

    test([[7],[9],[6]])
