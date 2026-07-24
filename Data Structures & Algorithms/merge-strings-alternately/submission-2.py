class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1 = len(word1)
        l2 = len(word2)
        newWord = []

        if l1 <= l2:
            for i in range(l1):
                newWord.append(word1[i])
                newWord.append(word2[i])
            if l2 > i:
                newWord.append(word2[i+1:])
        else:
            for i in range(l2):
                newWord.append(word1[i])
                newWord.append(word2[i])
            if l1 > i:
                newWord.append(word1[i+1:])
        return "".join(newWord)


"""
Recorro ambas listas hasta que se acabe la mas pequeña
Voy agregando uno y uno en la nueva string

Si queda de alguna lo agrego

"""
        