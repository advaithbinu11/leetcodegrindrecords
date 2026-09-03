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
#Failed attempt
class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        if(k!=0):
            j = len(nums)-k
            i = 0
            while(i<j):
                save=nums[i]
                nums[i] = nums[j]
                nums[j] = save
                i+=1
                j+=1
                if(j == len(nums)):
                    j = len(nums)-k
