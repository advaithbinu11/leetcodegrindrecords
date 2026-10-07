class Solution:
    def reverseWords(self, s: str) -> str:
        strArr = s.split(" ")
        res = ""
        for i in range(len(strArr)-1,-1,-1):
            if(len(strArr[i]) != 0):
                res+=strArr[i]
                res+=" "
        return res.strip()
