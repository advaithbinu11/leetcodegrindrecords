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

# Fixed KMP Attempt
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        i = 1
        parr = [0] * len(needle)
        while(i < len(needle)):
            if(needle[i] == needle[j]):
                j+=1
                parr[i] = j
            else:
                if j!= 0:
                    j = parr[j-1]
                    i-=1
            i+=1
        j=0
        i=0
        print(parr)
        while(i< len(haystack)):
            if(haystack[i] == needle[j]):
                j+=1
                if(j == len(needle)):
                    return i-(len(needle)-1)
            elif (j != 0):
                j = parr[j-1]
                i-=1
            i+=1
        return -1

