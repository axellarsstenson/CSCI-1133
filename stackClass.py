


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
            return self.slist[len(self.slist)]

    def __str__(self):                              ##overloads str for printing
        s = ""
        while self.isempty() == False:
            s = s + self.pop()
            if not self.isempty():
                s = s + " "               
        return s



def main(sString):                  

    stringStack = Stack()
    
    for i in range(len(sString)):
        stringStack.push(sString[i])

    print(stringStack)



main("python!")






