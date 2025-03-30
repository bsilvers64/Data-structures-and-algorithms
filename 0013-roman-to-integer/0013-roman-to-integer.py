class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_num = {
            'I'      :       1,
            'V'      :       5,
            'X'      :       10,
            'L'      :       50,
            'C'      :       100,
            'D'      :       500,
            'M'      :       1000
        }

        result = 0
        i = 0

        while i < len(s)-1:
            if roman_to_num[s[i]] >= roman_to_num[s[i+1]]:
                result += roman_to_num[s[i]]
                i +=1
            else:
                result += (roman_to_num[s[i+1]] - roman_to_num[s[i]])
                i += 2

        if i == len(s)-1: result += roman_to_num[s[i]]

        return result
