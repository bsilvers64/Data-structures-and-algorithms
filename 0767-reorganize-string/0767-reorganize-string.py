class Solution:
    def reorganizeString(self, s: str) -> str:
        ans = ""
        count = collections.Counter(s)
        print(count)
        heap = []
        for k, v in count.items():
            heapq.heappush(heap, [-v, k])

        while heap:
            temp1 = heapq.heappop(heap)
            ans += temp1[1]
            temp1[0] += 1
            if heap:
                temp2 = heapq.heappop(heap)
                ans += temp2[1]
                temp2[0] += 1
                if temp2[0]: heapq.heappush(heap, temp2)
            if temp1[0]: heapq.heappush(heap, temp1)

        print(ans)
        for i in range(1, len(ans)):
            if ans[i] == ans[i-1]: return ""
        return ans
