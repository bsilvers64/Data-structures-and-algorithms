class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # if endword not in given list, then not possible to transform
        if endWord not in wordList: return 0

        # maps patterns to a list of words that match that pattern
        pattern_to_words = defaultdict(list)

        # going through every word, creating all possible patterns
        # and appending words to those pattern - keys
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_to_words[pattern].append(word)
        
        # start a Breadth-first-search starting the given beginWord
        queue = deque()
        steps = 1
        queue.appendleft(beginWord)
        visited = set()

        while queue:

            # processing a level in BFS - 
            for _ in range(len(queue)):
                word = queue.pop()

                # if word is endWord, means we finally transformed our beginWord
                # so return the number of steps to reach this
                if word == endWord:
                    return steps

                # going through all patterns given by this word
                # and adding words that match those patterns, i.e. adding words
                # the next level of BFS that differ to current word by 1 character

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]

                    for similar_word in pattern_to_words[pattern]:
                        if similar_word not in visited:
                            queue.appendleft(similar_word)
                            visited.add(similar_word)
                    
                    # deleting pattern to avoid redundant exploring
                    del pattern_to_words[pattern] 
            
            # increment steps after processing each level
            # each level represents all words differing to the previous level word by 1 character
            steps += 1

        # in case we reach here, means we couldn't tranform our word
        return 0



