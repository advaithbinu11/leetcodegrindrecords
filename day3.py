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
