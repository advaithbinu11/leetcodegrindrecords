def isAlphanumeric(c):
    return (ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c)>=ord('0') and ord(c)<=ord('9'))
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i = 0
        j = len(s)-1
        while(i<j):
            if(s[i]==s[j]):
                i+=1
                j-=1
            elif (not isAlphanumeric(s[i])):
                i+=1
            elif (not isAlphanumeric(s[j])):
                j-=1
            else:
                return False
        return True
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j = 0
        if (len(s)==0):
            return True
        for i in range(0, len(t)):
            if(t[i] == s[j]):
                j+=1
                if(j == len(s)):
                    return True
        return False
class Solution:
    def reverseBits(self, n: int) -> int:
        s = ""
        j =32
        while(n>0):
            bit = n % 2
            s += str(bit)
            n //= 2
            j-=1
        while(j>0):
            s += "0"
            j-=1
        print(s)
        return int(s,2)
class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        j = 32
        while(n>0):
            bit = n & 1
            res <<= 1
            res |= bit
            n >>= 1
            j-=1
        res <<= j
        return res
class Solution:
    def romanToInt(self, s: str) -> int:
        i = len(s)-1
        dicti = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        sum = 0
        while (i>=0):
            if(i>0 and dicti[s[i]]>dicti[s[i-1]]):
                sum+=(dicti[s[i]]-dicti[s[i-1]])
                i-=2
            else:
                sum+=dicti[s[i]]
                i-=1
        return sum
        # Failed 
    class Solution:
        def removeDuplicates(self, nums: List[int]) -> int:
            i = 0
            j = 1 
            numDups = 0
            while(j<len(nums)-numDups):
                if(nums[i]==nums[j] and j-i == 2):
                    numDups += 1
                    for k in range(j, len(nums)-1):
                        save = nums[k]
                        nums[k] = nums[k+1]
                        nums[k+1] = save
                    j-=1
                if(nums[i]==nums[j]):
                    j+=1
                else:
                    i = i+1
                    j = i +1
            return len(nums) - numDups
    #Fixed
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        numDups = 0
        for num in nums:
            if(k<2 or num != nums[k-2]):
                nums[k] = num
                k+=1
            else:
                numDups += 1
        return len(nums) - numDups
