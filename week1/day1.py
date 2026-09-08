class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freqdict = {}
        max = nums[0]
        for i in range(0, len(nums)):
            if(freqdict.get(nums[i], None) == None):
                freqdict[nums[i]] = 1
            else:
                freqdict[nums[i]] = freqdict[nums[i]] + 1
                if(freqdict[max]<freqdict[nums[i]]):
                    max=nums[i]
        return max
# second solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max = nums[0]
        count = 0
        for i in range(0, len(nums)):
            if(nums[i]==max):
                count+=1
            else:
                count-=1
                if(count == 0):
                    max = nums[i]
                    count = 1
        return max
            
  class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if(len(a)<len(b)):
            c = a
            a = b
            b = c
        s = ""
        store = 0
        bi = 0
        for i in range(0, len(a)):
            ai = int(a[len(a)-i-1])
            if(i<len(b)):
                bi = int(b[len(b)-i-1])
            sum = ai + bi + store
            if(sum % 2 == 0):
                s = str(0)+s
            else:
                s = str(1)+s
            if(sum>=2):
                store = 1
            else:
                store = 0
            bi = 0
            ai = 0
        if(store == 1):
            s = str(1)+s
        return s

            
