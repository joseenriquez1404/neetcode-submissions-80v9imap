from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict()

        for s in strs:
            ss = ''.join(sorted(s))
            if ss not in anagrams:
                anagrams[ss] = [s]
            else:
                anagrams[ss].append(s)

        return list(anagrams.values())