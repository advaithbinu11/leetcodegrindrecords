class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        startStation = 0
        surplus = 0
        total = 0
        for i in range(len(gas)):
            surplus += gas[i]-cost[i]
            total += gas[i]-cost[i]
            if(surplus<0):
                startStation = i+1
                surplus = 0
        if total<0:
            return -1
        else:
            return startStation
