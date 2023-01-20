class Solution:
    def customSortString(self, S: str, T: str) -> str:
        d = {k : i for i, k in enumerate(S)}
        return ''.join(sorted(T, key=lambda k: d.get(k, len(T) + ord(k))))
