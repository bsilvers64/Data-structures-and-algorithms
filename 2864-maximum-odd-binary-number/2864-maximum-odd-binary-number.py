class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        total = len(s)
        one_count = 0
        
        for i in s: 
            if i == "1": 
                one_count += 1
        ans = []
        zero_count = total - one_count
        one_count -= 1
        while one_count:
            ans.append("1")
            one_count -= 1

        while zero_count:
            ans.append("0")
            zero_count -= 1

        ans.append("1")
        return "".join(ans)