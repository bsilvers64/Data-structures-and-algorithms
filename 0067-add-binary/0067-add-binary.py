class Solution:
    def addBinary(self, a: str, b: str) -> str:
        num1 = 0
        num2 = 0

        n = len(a)-1
        for i in a:
            if i == '1':
                num1 += pow(2, n)
            n-=1

        n = len(b)-1
        for i in b:
            if i == '1':
                num2 += pow(2, n)
            n-=1
        
        num = num1+num2
        if not num: return "0"
        binary_string = ""
    
        while num > 0:
            remainder = num % 2  # Get the remainder (either 0 or 1)
            binary_string = str(remainder) + binary_string  # Add remainder to the front
            num = num // 2  # Perform integer division by 2
        
        return binary_string