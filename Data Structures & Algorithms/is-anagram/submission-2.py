from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s1 = defaultdict(int)
        s2 = defaultdict(int)

        for c in s:
            if c in s1:
                s1[c] += 1
            else:
                s1[c] = 1

        for c in t:
            if c in s2:
                s2[c] += 1
            else:
                s2[c] = 1

        return s1 == s2