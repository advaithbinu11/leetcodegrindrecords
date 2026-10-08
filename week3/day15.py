class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split("/")
        res = "/"
        pathStack = []
        for s in pathArr:
            if(len(s) > 0 and s != "." and s != ".."):
                pathStack.append(s)
            elif(s == ".." and len(pathStack) > 0):
                pathStack.pop()   
        for sa in pathStack:
            res += sa + "/"
        return ("/" if res == "/" else res[:-1])
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sums = [0] * len(nums)
        sums[0] = nums[0]
        if(sums[0] >= target):
            return 1
        minLen = len(nums) + 1
        for i in range(1, len(nums)):
            sums[i] = nums[i] + sums[i-1]
            if(sums[i] >= target):
                minLen = min(minLen, i + 1)
        if(sums[0] >= target):
            return 1
        elif(minLen > len(nums)):
            return 0
        left = 1
        right = 1
        while(right < len(nums)):
            curr = sums[right] - sums[left-1]
            if(curr >= target):
                minLen = min(minLen, right-left+1)
                left += 1
            else:
                right+=1
        minLen = min(minLen, len(nums))
        return minLen
