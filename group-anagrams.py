#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def groupAnagrams(self, strs):
        ret, seq = [], {}
        for str in strs:
            s = ''.join(sorted(str))
            if s not in seq:
                seq[s] = len(ret) - 1
                ret.append([s])
            ret[seq[s]].append(s)
        return ret

    def groupAnagrams2(self, strs):
        ret = {}
        for str in strs:
            s = ''.join(sorted(str))
            d = ret.get(s, [])
            d.append(str)
            ret[s] = d
        return ret.values()


if __name__ == '__main__':
    so = Solution()


    def test(n):
        print 'origin:', n, ' ret:\n', so.groupAnagrams(n)


    test(["eat", "tea", "tan", "ate", "nat", "bat"])
    test([])
    test(['a', 'b', 'c'])
    test(['ab', 'ba'])
    test(['akka', 'aka', 'aak', 'kka'])
