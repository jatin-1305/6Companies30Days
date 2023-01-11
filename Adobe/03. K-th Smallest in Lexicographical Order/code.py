class Solution:
    def findKthNumber(self, n, k):
        if k == 1: return 1
        return self.denary(n, k)

    def denary(self, n, k):
        cur = 1  # cur starting from 1
        k -= 1  # k-th shift to 0-indexed

        while k > 0:  # final goal : find cur when k is cutted down to 0
            counts = self.counts_lte(n, cur)

            if counts <= k:  # final answer is not under current number, go right!
                k, cur = k - counts, cur + 1
            else:  # answer is under current number prefix, go in down~
                k, cur = k - 1, cur * 10

        return cur  # at this moment, k is zero, the final prefix cur is what we want

    def counts_lte(self, n, num):  # counts less or equal than num
        counts, limit = 0, num + 1

        while num <= n:  # sum total counts layer by layer untill num is greater than n
            counts += min(n + 1, limit) - num  # notice: n is another limit boundary when calculating counts
            num, limit = num * 10, limit * 10  # next layer

        return counts
