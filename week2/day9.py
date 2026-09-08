class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumps = [False] * len(nums)
        i = len(nums)-1
        while(i>=0):
            if(i+nums[i]>=len(nums)-1):
                jumps[i] = True
            else:
                for j in range(1, nums[i]+1):
                    if(jumps[i+j]):
                        jumps[i] = True
            i-=1
        return jumps[0]
#Optimized Greedy Algorithm
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if(i+nums[i]>=goal):
                goal = i
        return goal == 0
