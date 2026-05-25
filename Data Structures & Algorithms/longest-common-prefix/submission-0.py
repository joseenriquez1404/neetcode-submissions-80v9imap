class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        strs = sorted(strs, key = len)

        for i in range(len(strs[0])):
            temp = prefix + strs[0][i]
            if all(s.startswith(temp) for s in strs):
                prefix = temp
            else:
                return prefix

        return prefix

"""
1. Primero sorterar por len

2. Escoger el primero, luego segundo del indice 0 y checar si los somas empiezan con ese


"""
        