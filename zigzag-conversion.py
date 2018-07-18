#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def convert(self, s, numRows):
        if not s or numRows == 1 or len(s) <= numRows:
            return s

        ret, slen = '', len(s)
        columns, rowIndexMax = (1 + slen / (2 * numRows -3)) * (numRows - 1), numRows - 1

        print 'columns:', columns, ' numRows:', numRows

        for i in xrange(numRows):
            j = 0
            while j < columns:
                index = None
                if j % rowIndexMax == 0:
                    index = 2 * j + i
                    if i == 0 or i == rowIndexMax:
                        j += rowIndexMax
                    else:
                        j += rowIndexMax - i
                elif (i + j) % rowIndexMax == 0:
                    index = 2 * j + i
                    j += i
                if index is not None and index < slen:
                    ret += s[index]
        return ret

    def convert2(self, s, numRows):
        if not s or numRows == 1 or len(s) <= numRows:
            return s

        slen = len(s)
        need = (slen - numRows) / (2 * numRows - 2) + 1

        c = 0
        columns = numRows * need
        p = []
        for j in range(columns):
            for i in range(numRows):
                if len(p) <= i:
                    p.append([None] * columns)
                if j % (numRows - 1) == 0 or (i + j) % (numRows - 1) == 0:
                    if c < slen:
                        p[i][j] = s[c]
                        print 'i:', i, ' j:', j, ' c:', c
                        c += 1

        ret = ''
        for i in range(numRows):
            for j in range(columns):
                if p[i][j] != None:
                    ret += p[i][j]
        return ret

    def printList(self, p):
        for i in range(len(p)):
            print(p[i])


if __name__ == '__main__':
    so = Solution()
    assert(so.convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI")
    assert(so.convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR")
    assert(so.convert("PAYPALISHIRING", 5) == "PHASIYIRPLIGAN")
    assert(so.convert("PAYPALISHIRING", 2) == "PYAIHRNAPLSIIG")
    assert(so.convert("PAYPALISHIRING", 7) == "PNAIGYRPIAHLSI")
    s = "ywczetioyvlyncqvnjvmpajtotpubyjbulayglneiafxcvsqepewrnpgggcjelmbypbeaqliqqhvlzlsqpqiefqnlsysfntdcwhenuodkvyywlsociwjnoyaiysnlnqnkatxuhchcdfaqxpvhneuccwkcraoeqdqsxppgswjxdlnaaijoodqsbcvscjxvmpplfesxcdwfojhpuqdivvdxzypcjozxeojjtbivggdupkllbqwwlzvnzlpibqffeqqztavzgywykhjlyhklifyhsprufzbmrslluimbiiztqkgquqbcycmqtfkbemnygyjchvdreekwrronjpphtdynjkopydnebyjkwmcctoymhmzrdqyzuwofjewhhmokkxxglbiepiqxwpqcgodcnrhwvffertoeqnmcovigfbfesviallcaelwbrcfkxvoojbsxyaffbkluftuteztkmslfwqqtmgjxhbwhecphmaduuapazillawtwpjsdpbazdwijaxqpyujswauvifijcbhrmzwebwfgunpvlhkldvfzvzwdfhojkyczxydauiioxzlkhvvmqamnakrfrhqefsddqifmqocpnoawlvjcyxpyhifbqxhxpkchuivkyxblnbizztdxqsxzdeavbjsqvvzpfuzdtdojeyidrlchfzhkfjfgtayqvxgcthfpkvypuiunvzvaaengpumkulbrkhtgoavzwvqsdmfyncaoinuyiikctlwgupmlqhmoccghqlfeohuyvowfyhjuufarxocpvodzsjgiwnomuilryhwxqgtnntekhgzeuefonnw"
    so.convert(s, 253)
