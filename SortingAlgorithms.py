## Merging two sorted arrays ##
# Time complexity: O(n)

def merge(left, right):

    leftPointer = rightPointer = 0
    result = []

    while leftPointer < len(left) and rightPointer < len(right):

        if left[leftPointer] <= right[rightPointer]:
            result.append(left[leftPointer])
            leftPointer += 1
        else:
            result.append(right[rightPointer])
            rightPointer += 1

    result.extend(left[leftPointer:])
    result.extend(right[rightPointer:])

    return result

## Design a merge sort algorithm ##
# Avergae time complexity: O(nlogn)

def merge_sort(array):

    if len(array) <= 1 :
        return array

    split = int(len(array)/2)

    #compute recursively
    left = merge_sort(array[:split])
    right = merge_sort(array[split:])

    return merge(left, right)

## Design a quick sort algorithm ##
# Avergae time complexity: O(nlogn)
from random import randint
def quick_sort(array):

    if len(array) <= 1:
        return array
    smaller, equal, larger = [],[],[]
    pivot = array[randint(0, len(array) - 1)]

    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quick_sort(smaller) + equal + quick_sort(larger)

## Design a bubble sort algorithm ##
# Average time complexity: O(n^2) 

def bubble_sort(array):

    if len(array) <= 1:
        return array
    
    for i in range(len(array)):
        j = i
        for j in range(len(array)):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j+1] = array[j]
                array[j] = temp
                
    return array

## Design a method that counts the number of inversions(swaps) needed to sort an array ##
# average time complexity: O(nlogn)

def countInversions(arr):
    return count_mergesort(arr)[1]

def count_mergesort(arr):
    if len(arr) == 1:
        return arr, 0
    
    
    split = int(len(arr)/2)
    left = arr[:split]
    right = arr[split:]
    left, ai = count_mergesort(left)
    right, bi = count_mergesort(right)

    inversions = 0 + ai + bi
    result = []
    i = j = 0   
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            inversions += (len(left)-i)
    result.extend(left[i:])
    result.extend(right[j:])
    return result, inversions

