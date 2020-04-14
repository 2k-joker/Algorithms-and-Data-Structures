### Steps for Implementing Karatsuba Multiplication Algorithm ###

#1. Break the two integers num1(a, b) and num2(c, d) 
#2. Recursively compute a*c $(ac)$
#3. Recursively compute b*d $(bd)$
#4. Recursively compute (a + b)(c + d) $(abcd)$
#5. Calculate (ab + bc) as (a + b)(c + d) – ac – bd 
#6. Let AC be ac with n zeros added to the end $(NumZerosA)$
#7. let ABCD be (ab + bc) with half n zeros added to the end $(NumZerosA)$
#8. The final answer is AC + ABCD + bd


def zeroAppend(numString, numZeros, left = True):
    #Append zeros either to the left or right of number
    for i in range(numZeros):
        if left:
            numString = '0' + numString
        else:
            numString = numString + '0'
    return numString

def K_Multiplication(num1, num2):
    
    #Convert both numbers to strings for easy access
    num1 = str(num1)
    num2 = str(num2)

    #Make base case to prevent infinite recursion
    if len(num1) == 1 and len(num2) == 1:
        return int(num1)*int(num2)
    if len(num1) < len(num2):
        num1 = zeroAppend(num1, len(num2)-len(num1))
    elif len(num1) > len(num2):
        num2 = zeroAppend(num2, len(num1)-len(num2))

    n = len(num1)
    m = n//2

    if(n%2) != 0:
        m += 1

    NumZerosB = n - m
    NumZerosA = NumZerosB * 2

    a = int(num1[:m])
    b = int(num1[m:])
    c = int(num2[:m])
    d = int(num2[m:])

    #Compute recursively
    ac = K_Multiplication(a, c)
    bd = K_Multiplication(b, d)
    abcd = K_Multiplication(a+b, c+d)
    AC = int(zeroAppend(str(ac), NumZerosA, False))
    ABCD = int(zeroAppend(str(abcd - ac - bd), NumZerosB, False))
    
    return AC + ABCD + bd







    
