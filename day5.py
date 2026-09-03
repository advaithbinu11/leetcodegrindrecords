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
