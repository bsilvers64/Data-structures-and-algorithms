class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        ans = []

        wordset = set(words)
        memo = {}

        def dfs(word):
            if word in memo: return memo[word]
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if ((prefix in wordset and suffix in wordset) or
                    prefix in wordset and dfs(suffix)):
                    memo[word] = True
                    return True
            
            memo[word] = False
            return memo[word]
        
        for word in words:
            if dfs(word):
                ans.append(word)

        return ans