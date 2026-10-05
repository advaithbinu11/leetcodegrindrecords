class Solution:
    def hammingWeight(self, n: int) -> int:
        res =0
        while(n>0):
            if(n%2==1):
                res+=1
            n//=2
        return res
class Solution:
    def candy(self, ratings: list[int]) -> int:
        distributions = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if(ratings[i] > ratings[i-1]):
                distributions[i] = 1 + distributions[i-1]
        res = 0
        for j in range(len(ratings)-2, -1, -1):
            if(ratings[j] > ratings[j+1]):
                distributions[j] = max(distributions[j], 1 + distributions[j+1])
            res += distributions[j]
        res += distributions[len(ratings)-1]
        return res
        
        
        
