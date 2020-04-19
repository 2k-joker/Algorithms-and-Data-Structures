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
#Time complexity: O(nlogn)

def merge_sort(array):

    if len(array) <= 1 :
        return array

    split = int(len(array)/2)

    #compute recursively
    left = merge_sort(array[:split])
    right = merge_sort(array[split:])

    return merge(left, right)





