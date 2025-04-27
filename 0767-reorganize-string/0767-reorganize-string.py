class Solution:
    def reorganizeString(self, s: str) -> str:
        count = defaultdict(int)
        for char in s: count[char] += 1
        N = len(s)

        maxchar, maxchar_count = '', 0
        for char, freq in count.items():
            if freq > maxchar_count:
                maxchar_count = freq
                maxchar = char
        
        if maxchar_count > ((N+1)//2): return ""

        result = [''] * len(s)

        i = 0
        while count[maxchar]:
            result[i] = maxchar
            count[maxchar] -= 1
            i += 2
        
        for char, freq in count.items():
            while freq:
                if i >= N: i = 1
                result[i] = char
                freq -= 1
                i += 2

        return "".join(result)