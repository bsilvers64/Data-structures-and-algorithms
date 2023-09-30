class Solution:
    def construct2DArray(self, o: List[int], m: int, n: int) -> List[List[int]]:
        if m*n != len(o):
            return []

        ans, k = [], 0
        for i in range(m):
            print(k*n,(k+1)*n-1)
            ans.append(o[k*n:(k+1)*n])
            k+=1
        return ans