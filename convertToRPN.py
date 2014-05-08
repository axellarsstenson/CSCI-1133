class Stack:
    def __init__(self):                             ##initializer
        self.slist = []

    def push(self, obj):                            ##appends to stack
        self.slist.append(obj)

    def isempty(self):                              ##true if empty stack
        return len(self.slist) == 0

    def pop(self):                                  ##returns popped element
        if self.isempty():
            return None
        else:
            return self.slist.pop()

    def peek(self):                                 ##returns last element
        if self.isempty():
            return None
        else:
            return self.slist[-1]

    def __str__(self):                              ##overloads str for printing
        s = ""
        while self.isempty() == False:
            s = s + self.pop()
            if not self.isempty():
                s = s + " "               
        return s




def convertToRPN(infix):

    operatorDic = {'(':0, ')':0, '+': 5, '-': 5, '*': 10, '/': 10}      ## Dictionary of op precidence
    numList = ['0','1','2','3','4','5','6','7','8','9']

    outputString = ""
    
    pStack = Stack()

    for item in infix:                                              ## Iterate over expression                                             

        if item in numList:                                         ## If number, add to output
            outputString = outputString + item

        else:

            if outputString != " ":                                 ## Add " " if item is not a number
                outputString = outputString + " "
            
            if item == "(":                                         ## Push "(" when found
                pStack.push(item)


            elif item in operatorDic:                               ## What to do with operators

                tempPrec = pStack.peek()
                while not pStack.isempty() and operatorDic[tempPrec] > operatorDic[item]:
                    outputString = outputString + pStack.pop()
                    if outputString[-1] != " ":
                        outputString = outputString + " "
                    if not pStack.isempty():
                        tempPrec = pStack.peek()
                        
                pStack.push(item)

            elif item == ")":                                       ## For ")", add to output if not "("

                while not pStack.isempty() and pStack.peek() != "(":
                    ouputString = outputString + pStack.pop()
                    
                if not pStack.isempty():                            ## Pop "("
                    pStack.pop()

    if outputString[-1] != " ":
        outputString = outputString + " "

    while not pStack.isempty():                                     ## Pop the rest of the stack and add
        if operatorDic[pStack.peek()] < 1:                          ## Add to stack if not "(" or ")"
            pStack.pop()
        else:
            outputString = outputString + pStack.pop() + " "

    if outputString[0] == " ":
        outputString = outputString[1:]
        
    return "\n" + outputString + "\n"
                       



def main():

    print(convertToRPN('2+3*6'))
    print(convertToRPN('(2+3)*6'))
    print(convertToRPN('24+3*6-4/212'))
    
    expression = str(input("Enter an arithmetic expression: "))
    print(convertToRPN(expression))



main()









