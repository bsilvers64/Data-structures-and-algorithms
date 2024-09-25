class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visit = set()
        deadends = {i for i in deadends}
        if target == "0000": return 0
        if "0000" in deadends: return -1
        q = collections.deque()
        visit.add("0000")
        q.append(["0000", 0])

        while q:
            num, moves = q.popleft()
            curr_num = list(map(int, num))
            for i in range(4):
                add = 1
                x = curr_num.copy()
                for _ in range(2):
                    curr_num[i] += add
                    if curr_num[i] == 10: curr_num[i] = 0
                    elif curr_num[i] == -1: curr_num[i] = 9
                    add = -1

                    temp = "".join(map(str, curr_num))

                    if temp not in visit and temp not in deadends:
                        if temp == target: return moves + 1
                        q.append([temp, moves+1])
                        visit.add(temp)                  
                    
                    curr_num = x.copy()
                 
        return -1


