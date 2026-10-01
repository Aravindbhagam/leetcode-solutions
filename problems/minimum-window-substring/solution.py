class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        freq = Counter(t)

        left = 0
        right = 0
        count = len(t)
        min_len = 2**32 - 1
        start = 0
        #growing logic
        while right < len(s):
            if freq[s[right]] > 0:
                count -= 1
            freq[s[right]] -= 1
            right += 1
            #shrinking logic
            while count == 0:
                if right - left < min_len:
                    min_len = right - left
                    start = left
                freq[s[left]] += 1
                if freq[s[left]] > 0:
                    count += 1
                left += 1
        return "" if min_len == 2**32 - 1 else s[start:start + min_len]