import re
class Solution:
    def distinctEchoSubstrings(self, text: str) -> int:
        return len(set(re.findall("(?=(.+)\\1)", text)))
