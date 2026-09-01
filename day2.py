class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if(len(needle)>len(haystack)):
            return -1
        aInd = 0
        bInd = 0
        while aInd<len(haystack):
            if(haystack[aInd] == needle[0]):
                save = aInd
                while(bInd<len(needle) and (aInd<len(haystack))):
                    if(haystack[aInd] != needle[bInd]):
                        aInd = save
                        bInd = 0
                        break
                    aInd+=1
                    bInd+=1
                if(bInd ==  len(needle)):
                    return aInd-len(needle)
            aInd+=1
        return -1
