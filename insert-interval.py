#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __repr__(self):
        return 's:' + str(self.start) + ' e:' + str(self.end)


class Solution(object):
    """
    思路2:先插入再排序后合并,参考merge-interval
    """
    def insert(self, intervals, newInterval):
        if not intervals:
            return [newInterval]

        ret, ist = [], False
        while intervals:
            last = ret[-1] if ret else None
            node = intervals.pop(0)
            if node.end < newInterval.start:
                if last and last.end >= node.start and last.start <= node.end:
                    last.start = min(last.start, node.start)
                    last.end = max(last.end, node.end)
                else:
                    ret.append(node)
            else:
                if node.end >= newInterval.start and node.start <= newInterval.end:
                    node.start = min(node.start, newInterval.start)
                    node.end = max(node.end, newInterval.end)
                    ist = True
                if last and last.end >= node.start and last.start <= node.end:
                    last.start = min(node.start, last.start)
                    last.end = max(node.end, last.end)
                else:
                    ret.append(node)
        if not ist:
            ret.append(newInterval)
            ret.sort(key=lambda x: x.start)
        return ret


if __name__ == '__main__':
    so = Solution()


    def test(l):
        ls = map(lambda x: Interval(x[0], x[1]), l)
        ls.sort(key=lambda x: x.start)
        n = Interval(6, 8)
        print 'origin:', ls, ' new:', n, 'ret:', so.insert(ls, n)


    test([[1, 4], [4, 5]])
    test([[1, 4]])
    test([[1, 4], [4, 5], [8, 10], [10, 15], [16, 19], [19, 20]])
    test([[1, 3], [2, 6], [8, 10], [15, 18]])
    test([[1, 4], [0, 4]])
    test([[1, 4], [0, 1]])
    test([[11, 14], [8, 10], [5, 6], [1, 4], [0, 0]])
    test([[1, 2], [3, 5], [9, 11]])
