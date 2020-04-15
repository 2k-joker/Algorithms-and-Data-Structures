## Design a method that checks if a string of brackets is balanced ##

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
