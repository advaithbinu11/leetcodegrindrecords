class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        s = str(x)
        i = 0
        j = len(s)-1
        while(i<j):
            if(s[i]!=s[j]):
                return False
            i+=1
            j-=1
        return True

#No string solution
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x!=0 and x%10==0)):
            return False
        rev = 0
        while (x>rev):
            digit = x%10
            rev = 10*rev + digit
            x//=10

        return x == rev or rev//10 == x
#Fixed it!!!
class Solution:
    @staticmethod
    def reverse(nums, i, j):
        while i < j:
            save = nums[i]
            nums[i] = nums[j]
            nums[j] = save
            i += 1
            j -= 1

    def rotate(self, nums: list[int], k: int) -> None:
        if len(nums) == 0:
            return

        k %= len(nums)

        if k != 0:
            self.reverse(nums, 0, len(nums) - 1)
            self.reverse(nums, 0, k - 1)
            self.reverse(nums, k, len(nums) - 1)

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(" ")
        dictwtp = {}
        dictptw = {}
        if(len(pattern)!=len(arr)):
            return False
        for i in range(0, len(pattern)):
            word = arr[i]
            pat = pattern[i]
            if(dictwtp.get(word, None) == None and dictptw.get(pat, None) == None):
                dictwtp[word] = pat
                dictptw[pat] = word
            elif((dictwtp.get(word, None) == None) or (dictptw.get(pat, None) == None)):
                return False
            elif(dictwtp[word] != pat or dictptw[pat] != word):
                return False
        return True
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict = {}
        if(len(s)!=len(t)):
            return False
        for i in range(0, len(s)):
            if(dict.get(s[i], None) == None):
                dict[s[i]] = 1
            else:
                dict[s[i]] += 1
        for i in range(0, len(t)):
            if(dict.get(t[i], None) == None):
                return False
            else:
                dict[t[i]] -= 1
                if(dict[t[i]]==-1):
                    return False
        return True

        
