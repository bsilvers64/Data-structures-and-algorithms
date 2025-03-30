class Solution:
    def intToRoman(self, num: int) -> str:
        roman = []

        q = num // 1000
        num %= 1000
        roman.append("M"*q)

        if 900 <= num < 1000:
            roman.append("CM")
            num %= 900


        q = num // 500
        num %= 500
        roman.append("D"*q)

        if 400 <= num < 500:
            roman.append("CD")
            num %= 400           


        q = num // 100
        num %= 100
        roman.append("C"*q)

        if 90 <= num < 100:
            roman.append("XC")
            num %= 90


        q = num // 50
        num %= 50
        roman.append("L"*q)

        if 40 <= num < 50:
            roman.append("XL")
            num %= 40

        q = num // 10
        num %= 10
        roman.append("X"*q)

        if num == 9:
            roman.append("IX")
            num %= 9
        

        q = num // 5
        num %= 5
        roman.append("V"*q)

        if num == 4:
            roman.append("IV")
            num %= 4
        
        q = num // 1
        num %= 1
        roman.append("I"*q)

        return "".join(roman)