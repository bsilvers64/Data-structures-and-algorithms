class Solution:
    def romanToInt(self, s: str) -> int:
        _map = {
            'I':             1,
            'V':             5,
            'X':             10,
            'L':             50,
            'C':             100,
            'D':             500,
            'M':             1000
        }

        total, i = 0, 0
        while i < len(s)-1:
            if _map[s[i]] >= _map[s[i+1]]:
                total += _map[s[i]]
                i += 1
            else:
                total += (_map[s[i+1]] - _map[s[i]])
                i += 2

        if i == len(s)-1: total += _map[s[i]]

        return total 