class Solution:
    def intToRoman(self, num: int) -> str:
        if(num == 0):
            return ""
        length = 0
        numS = num
        while(numS>9):
            length += 1
            numS//=10
        length+=1
        if(numS == 4):
            if(length == 1):
                num -= 4
                return "IV"
            elif(length == 2):
                num -= 40
                return "XL" + self.intToRoman(num)
            else:
                num -= 400
                return "CD" + self.intToRoman(num)
        elif(numS == 9):
            if(length == 1):
                num -= 9
                return "IX"
            elif(length == 2):
                num -= 90
                return "XC" + self.intToRoman(num)
            else:
                num -= 900
                return "CM" + self.intToRoman(num)
        elif(numS >= 5):
            if(length == 1):
                num -= 5
                return "V" + self.intToRoman(num)
            elif(length == 2):
                num -= 50
                return "L" + self.intToRoman(num)
            else:
                num -= 500
                return "D" + self.intToRoman(num)
        else:
            if(length == 1):
                num -= numS
                return "I" * numS
            elif(length == 2):
                num -= (numS * 10)
                return numS * "X" + self.intToRoman(num)
            elif(length == 3):
                num -= (numS * 100)
                return numS * "C" + self.intToRoman(num)
            else:
                num -= (numS * 1000)
                return numS * "M" + self.intToRoman(num)

            
        
