class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        res = 0

        for i, height in enumerate(heights):
            start = i
            while stack and height < stack[-1][0]:
                h, j = stack.pop()
                w = i - j
                area = w * h
                res = max(area, res)
                start = j
            
            stack.append([height, start])
        
        N = len(heights)
        while stack:
            h, i = stack.pop()
            w = N - i
            area = h * w
            res = max(area, res)
            

        return res