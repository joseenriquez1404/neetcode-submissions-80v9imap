class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        size = 0
        ans = 0
        ss = []

        while r < len(s):
            if s[r] not in ss:
                ss.append(s[r])
                size += 1
                r += 1
            else:
                ans = max(ans, size)
                if size - 1 > 0:
                    size = size - 1
                else:
                    size = 0
                ss.pop(0)
                l += 1

        return max(ans, size)