class Solution:
    def isHappy(self, n: int, curr=None) -> bool:
        if curr is None:
            curr = set()
        if n in curr:
            return False
        curr.add(n)
        sum = 0
        while n>0:
            sum += ((n%10)**2)
            n//=10
        if(sum == 1):
            return True
        return self.isHappy(sum, curr)
        
