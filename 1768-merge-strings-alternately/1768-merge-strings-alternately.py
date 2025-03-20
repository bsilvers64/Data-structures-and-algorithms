class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        l1, l2 = len(word1), len(word2)

        i, j = 0, 0
        while i < l1 or j < l2:
            c1 = word1[i] if i < l1 else None
            c2 = word2[j] if j < l2 else None
            if c1: result.append(c1)
            if c2: result.append(c2)
            i += 1
            j += 1

        return "".join(result)