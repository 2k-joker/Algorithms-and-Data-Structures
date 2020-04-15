## Design a method that checks if a string of brackets is balanced ##
# {[()]} : True ______ {{[]()}} : True ______ {([)]} : False
def isBalanced(s):
    
    if len(s) < 2:
        return "NO"
 
    d = {'}':'{', ']':'[', ')':'('}
    case = "{(["
    temp = []
    for i in s:
        if i in case:
            temp.append(i)
        else:
            if len(temp):
                return "NO"
            c = temp.pop()
            if c != d[i]:
                return "NO"
    if len(temp)!=0:
        return "NO"
    else:
        return "YES"

## Implement a stack ##

class Stack(object):
    def __init__(self):
        self.stack = []        
    
    def peek(self):
        if len(self.stack) < 1:
            return []
        tail = len(self.stack)-1
        return self.stack[tail]        
        
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()        
        
    def put(self, value):
        self.stack.append(value)
        
        
## Implement a queue with a stack methods ##

class Queue(object):
    def __init__(self):
        self.stack = []        
    
    def peek(self):
        if len(self.stack) < 1:
            return []
        return self.stack[0]        
        
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop(0)        
        
    def put(self, value):
        self.stack.append(value)
