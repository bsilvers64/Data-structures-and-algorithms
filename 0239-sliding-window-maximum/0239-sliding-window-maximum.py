class Solution:
    def maxSlidingWindow(self, A: List[int], B: int) -> List[int]:
        i, j, temp, ans = 0, 0, [], []
        heapq.heapify(temp)
		
        while (i < len(A)):
            heapq.heappush(temp, [-A[i], i])
            if (i - j + 1 == B):
                if j <= temp[0][1]:
                    ans.append(-temp[0][0])
                else:
                    while temp[0][1] < j:
                        heapq.heappop(temp)
                    #print(temp, j)
                    ans.append(-temp[0][0])

                if A[j] == -temp[0][0]: heapq.heappop(temp)
                j += 1
            i += 1
        return ans