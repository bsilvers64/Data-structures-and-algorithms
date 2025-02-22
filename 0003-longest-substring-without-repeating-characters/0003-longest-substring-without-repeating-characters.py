class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # tracks the count of each character appearing in the string
        character_frequency = defaultdict(int)

        l = 0
        r = 0

        max_length = 0

        while r < len(s):

            # increase the current character's count
            character_frequency[s[r]] += 1

            # if the window size is greater than the number of elements in our map
            # it means than we have duplicate elements, so we shrink our window
            while (r-l+1) > len(character_frequency) :
                character_frequency[s[l]] -= 1
                if character_frequency[s[l]] == 0:
                    del character_frequency[s[l]]
                l += 1

            # track max length of the substring
            max_length = max(max_length, r-l+1)
            r += 1

        return max_length

