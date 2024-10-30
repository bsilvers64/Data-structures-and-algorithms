class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitToChar = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        if digits == "": return []

        def backtrack(i, curr):
            if len(curr) == len(digits): 
                res.append(curr)
                return
            
            for j in range(len(digitToChar[digits[i]])):
                temp = digitToChar[digits[i]][j]
                backtrack(i+1, curr + temp)


        backtrack(0, "")
        return res