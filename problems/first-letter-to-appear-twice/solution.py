class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = {}
        for i in range(len(s)):
            if s[i] in freq:
                return s[i]
            freq[s[i]] = 1

        return ""