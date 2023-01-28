class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        seen = set()
        return self.helper(s, seen)

    def helper(self, s, seen):
        ans = 0
        if s:
            for i in range(1, len(s) + 1):
                candidate = s[:i]
                if candidate not in seen:
                    seen.add(candidate)
                    ans = max(ans, 1 + self.helper(s[i:], seen))
                    seen.remove(candidate)
        return ans
