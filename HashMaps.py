## Write a function that returns the intersection between two arrays of numbers ##

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

## Design a function that finds the number of pairs of digits in an array ##

def sockMerchant(n, ar):
    dictionary = dict()
    pairs = 0
    for i in range(n):
        
        if i in dictionary :
            if dictionary[i] % 2 == 0 :
                pairs +=1
            dictionary[i] +=1
            
        else:
            dictionary[i] = 1
    return pairs

### Design an algorithm that finds the number of anagrams in given string ###
## METHOD1
# Average time complexity: O(n^4)

def sherlockAndAnagrams(s):
    
    if len(s) <= 1:
        return 0

    arr = split_string(s)
    count = 0
    
    for i in range(len(arr)):
        count += countAnagrams(i, arr)
    
    return count
        

def countAnagrams(index, arr):

    count = 0
    current = arr[index]
    rest = arr[index+1:]

    for i in range(len(rest)):
        if len(rest[i]) == len(current) and isAnagram(current, rest[i]):
            count += 1
                
    return count

def split_string(string):
    if len(string) <= 1:
        return string

    result = []
    i = j = 0

    while i < len(string):
        j = i + 1
        while j < len(string)+1:
            result.append(string[i:j])
            j+= 1
        i += 1
    
    return result

def isAnagram(string1, string2):

    substrings = dict()

    for x in string1:
        if x in substrings:
            substrings[x] += 1
        else:
            substrings[x] = 1

    for x in string2:
        if x in substrings and substrings[x] > 0:
            substrings[x] -= 1
        else:
            return False
    return True

## Method2
# Average time complexity O(n^3)
def sherlockAndAnagrams(s):

    if len(s) <= 1:
        return 0

    keys = dict()
        
    for start in range(len(s)):

        for finish in range(start, len(s)):            
            key = [0]*26

            for char in s[start:finish+1]:
                key[ord(char)-ord('a')] += 1

            # tuples are hashable in contrast to lists
            key = tuple(key)
            keys[key] = keys.get(key,0) + 1

    result = 0

    for count in keys.values():
        result += int(count*(count-1)/2)

    return result

## Design a function that runs a list of queries and returns the result (Frequency query on hackerrank) ##
# Average time complexity: O(n)

from collections import defaultdict
def freqQuery(queries):

    if len(queries) == 0:
        return None

    keys = defaultdict(int)
    key_freq = defaultdict(int)
    result = []

    for q,val in queries:
        
        if q == 1:
            if key_freq[keys[val]]:
                key_freq[keys[val]] -= 1

            keys[val] += 1
            key_freq[keys[val]] += 1
            
        elif q == 2:
            if keys[val]:
                key_freq[keys[val]] -= 1
                keys[val] -= 1
                key_freq[keys[val]] += 1
        
        elif q == 3:
            if val in key_freq and key_freq[val] > 0:
                result.append(1)
            else: result.append(0) 

    return result

### Design a method that counts and returns the occurrance of each query string in a a given array of strings ###
### Sparse arrays problem on hackerrank ###
# Time complexity: O(n)
def matchingStrings(strings, queries):
    if not len(strings):
        return [0]

    table = dict()

    for s in strings:
        if s in table:
            table[s] += 1
        else:
            table[s] = 1
    
    result = []
    for q in queries:
        if q in table:
            result.append(table[q])
        else:
            result.append(0)
    return result
 

