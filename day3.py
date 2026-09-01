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
