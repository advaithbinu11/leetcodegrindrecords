class Solution:
    def isHappy(self, n: int, curr=None) -> bool:
        if curr is None:
            curr = set()
        if n in curr:
            return False
        curr.add(n)
        sum = 0
        while n>0:
            sum += ((n%10)**2)
            n//=10
        if(sum == 1):
            return True
        return self.isHappy(sum, curr)
        
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if(len(nums)==0):
            return []
        currS = str(nums[0])
        start = nums[0]
        for i in range(1, len(nums)):
            if(nums[i]-nums[i-1] != 1 and nums[i-1]!=start):
                currS+="->"
                currS+=str(nums[i-1])
                res.append(currS)
                currS = str(nums[i])
                start = nums[i]
            elif(nums[i]-nums[i-1] != 1 and nums[i-1]==start):
                res.append(currS)
                currS = str(nums[i])
                start = nums[i]
        if(start == nums[len(nums)-1]):
                res.append(currS)
        else:
            currS+="->"
            currS+=str(nums[len(nums)-1])
            res.append(currS)
        return res

            
