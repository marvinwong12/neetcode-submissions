class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest_len = 0
        l = 0
        seen = dict()

        for r in range(len(s)):
            if s[r] in seen:
                l = max(seen[s[r]] + 1, l)
            seen[s[r]] = r
            longest_len = max(longest_len, r - l + 1)

        return longest_len