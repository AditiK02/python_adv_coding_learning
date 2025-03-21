class stackbasic:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        return self.stack.append(item)

    def pop(self):
        if not self.isempty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.isempty():
            return self.stack[-1]
        return None
    
    def isempty(self):
        return len(self.stack)==0

stack1=stackbasic()
stack1.push(4)
stack1.push(45)
print(stack1.peek())



#----PARENTHESIS MATCH----
class parenthesismatch:
    def __init__(self):
        self.stack=[]

    def is_match(self,expression):
        matchingDict={ ')':'(','}':'{',']':'[' }
        for char in expression:
            if char in matchingDict.values():
                self.stack.append(char)
            elif char in matchingDict.keys():
                if self.stack ==[] or matchingDict[char] != self.stack.pop():
                    return False
        return self.stack

match1=parenthesismatch()
exp="[()]"
print(match1.is_match(exp))


# #---POSTFIX EXP EVALUATION---
# class postfixeval:
#     def __init__(self):
#         self.stack=[]
    
#     def evaluation(self,expression):
#         if len(expression)==0:
#             return None
#         for char in expression.split(" "):
#             if char.isdigit():
#                 self.stack.append(int(char))
#             else:
#                 op2=self.stack.pop()
#                 op1=self.stack.pop()
#                 if char=='+':
#                     self.stack.append(op2+op1)
#                 elif char=='-':
#                     self.stack.append(op2-op1)
#                 elif char=='*':
#                     self.stack.append(op2*op1)
#                 elif char=='/':
#                     self.stack.append(op2/op1)
#         return self.stack.pop()
    
# eval1=postfixeval()
# exp="2 3 +"
# print(eval1.evaluation(exp))               

#--TODO--
def infixtopostfix(expression):
    pass



            
            
