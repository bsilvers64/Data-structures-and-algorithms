class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        st = []
        MOD = 10**9 + 7

        N = len(arr)
        ans = 0

        for i, x in enumerate(arr):
            while st and x < st[-1][0]:
                temp = st.pop()
                # left and right occurances for the popped element -
                right = i - temp[1]
                left = temp[1] - st[-1][1] if st else temp[1] + 1
                ans = (ans + left * right * arr[temp[1]]) % MOD
            st.append([x, i])

        while st:
            temp = st.pop()
            left = temp[1] - st[-1][1] if st else temp[1] + 1
            right = N - temp[1]
            ans = (ans + left * right * arr[temp[1]]) % MOD

        return ans