class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        
        max_letter, max_count = '', 0
        for c, freq in count.items():
            if freq > max_count:
                max_letter = c
                max_count = freq
        

        if max_count > ((len(s)+1)//2): return ""

        result = [''] * len(s)

        index = 0

        while count[max_letter] != 0:
            result[index] = max_letter
            count[max_letter] -= 1
            index += 2


        for char, freq in count.items():
            while freq:
                if index >= len(s): index = 1
                result[index] = char
                freq -= 1
                index += 2

        return "".join(result) 