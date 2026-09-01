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

# Failed KMP Attempt
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        j = 0
        parr = [0] * len(needle)
        for i in range(1, len(needle)):
            if(needle[i] == needle[j]):
                parr[i] = parr[i-1]+1
                j+=1
            else:
                if j!= 0:
                    j = parr[j-1]
                else:
                    parr[i] = 0
                    i+=1
        j=0
        print(parr)
        for i in range(0, len(haystack)):
            if(haystack[i] == needle[j]):
                print("Hit " + str(i)+" "+str(j))
                j+=1
                if(j == len(needle)):
                    return i-(len(needle)-1)
            elif (j != 0):
                print(parr[j-1])
                j = parr[j-1]
        return -1
