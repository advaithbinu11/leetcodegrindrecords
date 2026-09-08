class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [0] * len(nums)
        for i in range(len(nums)-2, -1, -1):
            for j in range(nums[i], 0, -1):
                if(i+j>=len(nums)-1):
                    jumps[i] = 1
                elif(jumps[i+j]!=0):
                    if(1+jumps[i+j]<jumps[i] or jumps[i]==0):
                        jumps[i] = 1+jumps[i+j]
        return jumps[0]
                        
        
