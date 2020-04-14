## Write a function that returns the intersection between two arrays of numbers ##
# With Hash maps
def findIntersection(array1, array2):
    dictionary = dict()
    result = []
    for n in array1:
        if n in dictionary:
            dictionary[n] +=1
        else:
           dictionary[n]=1
    for n in array2:
        if n in dictionary and dictionary[n]>0:
            result.append(n)
                
    return result

## Write a function that takes an array and return its longest range of numbers ##
# With hash maps

def findLongestRange(array):
    table = dict()
    longestRange = 0
    
    for n in array:
        table[n] = False

    for n in array:
        if not table[n]:
            upper = n + 1
            lower = n - 1
            while upper in table:
                table[upper] = True
                upper += 1
            while lower in table:
                table[lower] = True
                lower -= 1
            currentRange = upper - lower
            if currentRange > longestRange:
                longestRange = currentRange
                max = upper - 1
                min = lower + 1
    result = [min, max]
    return result

## Design a method that counts the occurrences of a given word in a book ##
# The book is given as an array of strings
# The frequency count should be an integer(obviously)
# The method should be reusable
#With hash maps

## NOTE: Python has a built-in library (Counter) that can implement this problem a lot easier ##
# refer to the documentation https://docs.python.org/3/library/collections.html to see how


def createDictionary(book):
    dictionary = dict()
    
    for word in book:
        if word in dictionary:
            dictionary[word] +=1
        else:
            dictionary[word] = 1
    return dictionary

def getFrequency(dictionary, word):

    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found"

### Design a function that checks if a string is a pemutation of a palindrome ###
#With hash maps

def isPalindromePemutation(text):
    dictionary = dict()
    text = text.replace(" ","").lower()
    for char in text:
        if char in dictionary:
            dictionary[char]+=1
        else:
           dictionary[char]=1

    foundOdd = False

    for i in dictionary:
        if dictionary[i] % 2 ==1:
            if foundOdd:
                return False
            foundOdd = True        
    return True

