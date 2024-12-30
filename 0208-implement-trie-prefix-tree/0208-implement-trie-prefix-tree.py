class Trie:

    def __init__(self):
        self.wordlist = collections.defaultdict()

    def insert(self, word: str) -> None:
        wordTrie = self.wordlist
        for c in word:
            if c not in wordTrie:
                wordTrie[c] = collections.defaultdict()
            wordTrie = wordTrie[c]
        wordTrie["-"] = True


    def search(self, word: str) -> bool:
        wordTrie = self.wordlist
        for c in word:
            if c in wordTrie:
                wordTrie = wordTrie[c]
            else: return False
        return "-" in wordTrie

    def startsWith(self, prefix: str) -> bool:
        wordTrie = self.wordlist
        for c in prefix:
            if c in wordTrie:
                wordTrie = wordTrie[c]
            else: return False        
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)