class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList: return 0

        nei = defaultdict(list)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)
        
        q = deque()
        res = 1
        q.appendleft(beginWord)
        visited = set()

        while q:
            for i in range(len(q)):
                word = q.pop()
                visited.add(word)
                if word == endWord: return res

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visited:
                            q.appendleft(neiWord)
            res += 1
                    
        return 0