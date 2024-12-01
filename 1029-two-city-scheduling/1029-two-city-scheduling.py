class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff, total, total_cost = [], 0, 0

        # total cost for sending all to A and,
        # checking the difference bewteen costs of sending to A vs cost of sending to B
        for cost in costs:
            total_cost += cost[0]
            diff.append(cost[1] - cost[0])
        
        # if the diff was +ve, means cost to B was higher
        # if the diff was -ve, means cost to A was higher
        # so if we add the -ve differences to our total cost, that would mean we sent that person to B instead
        # and we will just send all the people with -ve differences to B instead. as they get lower costs

        # sort by max -ve differences
        diff.sort()

        # only send N//2 half the number of people to B
        N = len(costs)//2
        for i in range(N):
            total_cost += diff[i]
        
        # total is now adjusted to people being sent to B instead where it was cheaper
        return total_cost
