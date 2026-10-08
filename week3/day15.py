class Solution:
    def simplifyPath(self, path: str) -> str:
        pathArr = path.split("/")
        res = "/"
        pathStack = []
        for s in pathArr:
            if(len(s) > 0 and s != "." and s != ".."):
                pathStack.append(s)
            elif(s == ".." and len(pathStack) > 0):
                pathStack.pop()   
        for sa in pathStack:
            res += sa + "/"
        return ("/" if res == "/" else res[:-1])
