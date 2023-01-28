class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n, ans, mod = len(nums), 0, 10 ** 9 + 7
        
        lft, st = [0], [[nums[0], 0]]       #how many valid numbers on its left 
        for i in range(1, n):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append([nums[i], cur])
            lft.append(cur)

        rgt, st = [0], [[nums[-1], 0]]               #how many valid numbers on its right 
        for i in range(n - 2, -1, -1):
            cur = 0
            while st and nums[i] <= st[-1][0]:
                cur += st.pop()[1] + 1
            st.append(([nums[i], cur]))
            rgt.append(cur)
        rgt.reverse()

        sums, cur = [0], 0           # presum array
        for i in range(n):
            cur += nums[i]
            sums.append(cur)

        for i in range(n):
            ans = max(ans, nums[i] * (sums[i + rgt[i] + 1] - sums[i - lft[i]]))

        return ans % mod
