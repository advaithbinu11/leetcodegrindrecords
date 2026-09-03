class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split()
        return len(arr[len(arr)-1])
        
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for i in range(0, len(magazine)):
            if dict.get(magazine[i], None) == None:
                dict[magazine[i]] = 1
            else:
                dict[magazine[i]] += 1
        for j in range(0, len(ransomNote)):
            if dict.get(ransomNote[j], None) == None:
                return False
            dict[ransomNote[j]] -= 1
            if dict[ransomNote[j]] == -1:
                return False
        return True
