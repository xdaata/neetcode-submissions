class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total = 0
        start = 0
        while True:
            for i in range(start, start + len(gas)):
                i = i % len(gas)

                total += gas[i] - cost[i]

                if total < 0:
                    total = 0
                    break

                if i == len(gas) - 1:
                    return start

            start = i + 1
            
        
        return -1      

