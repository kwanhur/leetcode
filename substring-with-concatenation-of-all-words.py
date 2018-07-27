#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def findSubstring(self, s, words):
        if not s and words:
            return []
        if not s and not words:
            return [0]

        slen = len(s)
        for w in words:
            if len(w) > slen or s.find(w) == -1:
                return []

        def arrange(wd0, total):
            if total == 1:
                return wd0

            ret, t = [], total - 1
            for i, w in enumerate(wd0):
                res = arrange(wd0[:i] + wd0[i + 1:], t)
                for item in res:
                    ret.append(w + item)
            return ret

        wds = arrange(words, len(words))
        wds = list(set(wds))

        ret = []
        for wd in wds:
            idx, st = 0, 0
            while True:
                idx = s.find(wd, st)
                if idx > -1:
                    ret.append(idx)
                    st = idx + 1
                else:
                    break
        return ret


if __name__ == '__main__':
    so = Solution()


    def test(s, ws):
        print 's:', s, 'ws:', ws, 'ret:', so.findSubstring(s, ws)


    test('barfoothefoobarman', ["foo", "bar"])
    test('barfoothefoobarman', ["foo"])
    test('wordgoodstudentgoodword', ['word', 'student'])
    test("wordgoodgoodgoodbestword", ["word", "good", "best", "good"])
    test("foobarfoobar", ["foo", "bar"])
    test("aaa", ['a', 'a'])
    test("aaaaaaaa", ['aa'] * 3)
