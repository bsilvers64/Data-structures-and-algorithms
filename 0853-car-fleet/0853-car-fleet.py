class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped_list = list(zip(position, speed))
        pos_speed = sorted(zipped_list, key=lambda x: x[0], reverse=True)
        st = []

        st.append((target-pos_speed[0][0])/pos_speed[0][1])

        for i in pos_speed[1:]:
            time_taken = (target-i[0])/i[1]
            if time_taken <= st[-1]: continue
            st.append(time_taken)
        
        print(st)
        return len(st)

