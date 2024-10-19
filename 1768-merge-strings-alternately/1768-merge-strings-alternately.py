class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = 0, 0
        N1, N2 = len(word1), len(word2)
        ans = []
        while l1 < N1 and l2 < N2:
            ans.append(word1[l1])
            ans.append(word2[l2])  # Corrected to append from word2
            l1 += 1
            l2 += 1
        
        while l1 < N1:
            ans.append(word1[l1])
            l1 += 1  # Add this increment

        while l2 < N2:
            ans.append(word2[l2])
            l2 += 1  # Add this increment
        
        print(ans)
        return ''.join(ans)
