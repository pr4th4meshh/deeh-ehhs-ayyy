class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        res = 0

        for i in range(len(s)):
            if s[i] in mp:
                left = max(mp[s[i]] + 1, left)
            mp[s[i]] = i
            res = max(res, i - left + 1)
        return res
        