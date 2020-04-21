## Swap is always handy for arrays

def swap(i, j, array):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

## Write a method that checks if two arrays of integers are pemutations of each other ##
# Time complexity: O(nlogn) or O(n) if done with hash maps(python dictionary)

def isPemutation(array1, array2):
    
    if len(array1) != len(array2):
        return False
    
    array1.sort()
    array2.sort()

    for i in array1:
        if array1[i] != array2[i]:
            return False
     
    return True

## Write a function to determine if an array has all unique elements ##
# Time complexity: O(nlogn) or O(n) with hash maps(python dictionary)

def isUnque(array):
    array.sort()

    for i in array:
        if array[i] == array[i+1]:
            return False

    return True

## Write a function that searches an array to find two numbers that sum up to a target integer ##
# Assume array of integers and that at most one  correct pair exists
# Time complexity: O(nlogn)

def twoIntegerSum(array, target):
    if len(array) < 2:
        
        return "Is you dumb??"

    array.sort()
    tail = len(array) - 1
    head = 0
    
    while head != tail:
        if array[head] + array[tail] == target:
            return [array[head], array[tail]]
        elif array[head] + array[tail] > target:
            tail -=1
        elif array[head] + array[tail] < target:
            head +=1
    return []

## Write a function that takes target number and moves it to the end of the array ##
# Time complexity: O(n)

from Reusables import swap
def moveToEnd(array, target):

    head = 0
    tail = len(array) - 1
    while head < tail :
        if array[tail] == target:
            tail -=1
        elif array[head] != target:
            head +=1
        else:
            swap(head, tail, array)
            head +=1
            tail -=1
    return array

## Write a function that determines how many times a larger element in a sorted array bribed a smaller element to switch positions ##
# Average time complexity O(nlogn)
def minimumBribes(arr):
    
    counter = 0

    for i in range(len(arr)):
        if q[i] - (i+1) > 2:
            return print("Too chaotic")
        for j in range(max(0,arr[i]-2),i):
            if arr[j] > arr[i]:
                counter += 1
    return print(counter)

## Design a function that finds the maximum number of toys that can be bought given an array of toy prices and max amount ##
# Average time complexity: O(nlogn)

def maximumToys(prices, k):
    if len(prices) ==0 or k <= 0:
        return 0
    k_and_under = []

    for x in prices:
        if x <= k:
            k_and_under.append(x)

    k_and_under.sort()
    max_toys = 0

    for i in range(len(k_and_under)):
        k -= k_and_under[i]
        if k < 0:
            return max_toys
        i += 1
        max_toys += 1

    return max_toys

