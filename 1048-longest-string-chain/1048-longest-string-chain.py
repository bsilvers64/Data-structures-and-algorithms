class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_predecessor(wordA, wordB):
            if len(wordB) != len(wordA) + 1:
                return False

            i, j = 0, 0
            mismatch_found = False

            while i < len(wordA) and j < len(wordB):
                if wordA[i] == wordB[j]:
                    i += 1
                elif not mismatch_found:
                    mismatch_found = True
                else: 
                    return False
                j += 1
            return True

        dp = [1] * len(words)
        words.sort(key=len)

        ans = 1
        for i in range(1, len(words)):
            for j in range(i):
                if is_predecessor(words[j], words[i]):
                    dp[i] = max(dp[i], 1 + dp[j])
            ans = max(ans, dp[i])
        
        return ans
