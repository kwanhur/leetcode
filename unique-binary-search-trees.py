#! /usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def numTrees(self, n):
        """
        左右子树节点分配方式:(0, n - 1) (1, n - 2) (2, n - 3) (n -1, 0)
        种类数:dp(0)*dp(n - 1) + dp(1) * dp(n -2) + dp(n-1)*dp(0)
        """

        dp = dict([(i,0) for i in xrange(n + 1)])
        dp[0], dp[1] = 1, 1
        for i in xrange(2, n + 1):#总节点数
            for j in xrange(i): #左子树节点数
                dp[i] = dp[i] + dp[j] * dp[i - j - 1] #所有子树种类加和
        return dp[n]


if __name__ == '__main__':
    so = Solution()

    def test(n):
        print 'n:', n, 'ret:', so.numTrees(n)

    test(1)
    test(2)
    test(3)
    test(4)
    test(5)

