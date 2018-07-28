#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return 's:' + str(self.start) + ' e:' + str(self.end)


class Solution(object):
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        lst = 0
        for idx in range(1, len(intervals)):
            node, last = intervals[idx], intervals[lst]
            if node.start <= last.end:
                last.start = node.start if last.start > node.start else last.start
                last.end = node.end if last.end < node.end else last.end
                intervals[idx] = None
                intervals[lst] = last
            else:
                lst = idx
        return filter(lambda x: x is not None, intervals)

    def merge2(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)
        ret = [intervals.pop(0)]
        while intervals:
            node, last = intervals.pop(0), ret[-1]
            if node.start <= last.end:
                # last.start, last.end = min(last.start, node.start), max(last.end, node.end)
                last.start = node.start if last.start > node.start else last.start
                last.end = node.end if last.end < node.end else last.end

            else:
                ret.append(node)
        return ret


if __name__ == '__main__':
    so = Solution()


    def test(l):
        ls = map(lambda x: Interval(x[0], x[1]), l)
        print 'origin:', ls, 'ret:', so.merge(ls)


    test([[1, 4], [4, 5]])
    test([[1, 4]])
    test([[1, 4], [4, 5], [8, 10], [10, 15], [16, 19], [19, 20]])
    test([[1, 3], [2, 6], [8, 10], [15, 18]])
    test([[1, 4], [0, 4]])
    test([[1, 4], [0, 1]])
    test([[11, 14], [8, 10], [5, 6], [1, 4], [0, 0]])
