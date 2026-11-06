class Solution:
    def canMerge(self, list1, list2) -> bool:
        maxS = max(list1[0], list2[0])
        minE = min(list1[1], list2[1])
        return maxS <= minE
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: (x[0], x[1]))
        print(intervals)
        curr = 0
        while (curr < len(intervals) - 1) :
            if self.canMerge(intervals[curr], intervals[curr + 1]) :
                newlist = [min(intervals[curr][0], intervals[curr+1][0]), max(intervals[curr][1], intervals[curr+1][1])]
                intervals.remove(intervals[curr])
                intervals.remove(intervals[curr])
                intervals.insert(curr, newlist)
            else :
                curr += 1
        return intervals
