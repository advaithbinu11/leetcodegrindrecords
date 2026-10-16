class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        opStack = []
        for i in range(0, len(tokens)):
            element = tokens[i]
            if(element == "+"):
                opStack.append(opStack.pop() + opStack.pop())
            elif(element == "-"):
                b = opStack.pop()
                opStack.append(opStack.pop() - b)        
            elif(element == "*"):
                opStack.append(opStack.pop() * opStack.pop())
            elif(element == "/"):
                b = opStack.pop()
                a = opStack.pop()
                res = a / b
                if(res >= 0):
                    opStack.append(floor(res))
                else:
                    opStack.append(ceil(res))
            else:
                opStack.append(int(element))
        return opStack.pop()
