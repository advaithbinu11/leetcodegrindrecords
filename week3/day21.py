class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        currW = len(matrix[0])
        currH = len(matrix)
        offSet = 0
        result = []
        target = currW * currH
        while (currW > offSet and currH > offSet):
            for i in range(offSet, currW):
                result.append(matrix[offSet][i])
            for i in range(offSet + 1, currH):
                result.append(matrix[i][currW-1])
            if(currH - 1 != offSet):     
                for i in range(currW-2, offSet-1, -1):
                    result.append(matrix[currH-1][i])
            if(currW - 1 != offSet):
                for i in range(currH-2, offSet, -1):
                    result.append(matrix[i][offSet])
            currW-=1
            currH-=1
            offSet+=1
        return result
