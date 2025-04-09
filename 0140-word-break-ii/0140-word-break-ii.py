class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset = set(wordDict)
        result = []
        temp = []
        N = len(s)

        def check(word):
            if not word:
                result.append(" ".join(temp))
                return True

            for i in range(1, len(word) + 1):
                prefix = word[:i]
                suffix = word[i:]

                if prefix in wordset:
                    temp.append(prefix)
                    check(suffix)
                    temp.pop()

        check(s)
        return result
