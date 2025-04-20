class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # dictionary where the key is the character frequency count array of a string
        # and value is a list of string that matches that frequency count array
        char_map = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            char_map[tuple(count)].append(word)
        
        # create a list of the anagrams
        group_anagrams = [anagrams for _, anagrams in char_map.items()]

        return group_anagrams