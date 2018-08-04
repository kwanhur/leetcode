#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def simplifyPath(self, path):
        if not path:
            return path

        ret = []
        for p in path.split('/'):
            if p == '..':
                if ret:
                    ret.pop(-1)
            elif p and p != '.':
                 ret.append(p)
        return '/' + '/'.join(ret)


if __name__ == '__main__':
    so = Solution()

    def test(p):
        print 'origin:', p, 'ret:', so.simplifyPath(p)

    test("/home/")
    test("/")
    test("/../")
    test("/a/")
    test("/home//foo/")
    test("/home/aa/./b/../../c/")
    test("/////")
    test("../../.././")

