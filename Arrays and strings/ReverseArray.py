'''
Given an array, reverse the order of its elements.
For example, [3,5,2,5,2,3,9] → [9,3,2,5,2,5,3]

Hint: Traverse array from start and end
'''

def reverseArr(arr):
    start = 0
    end = len(arr) - 1
    while (start<end):
        swap(arr, start, end)
        start = start + 1
        end = end - 1
    return arr

def swap(arr, start, end):
    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp
    return arr

arr = [3,5,2,5,2,3,9]
print(arr)
print(reverseArr(arr))

arr = []
print(arr)
print(reverseArr(arr))

arr = [3]
print(arr)
print(reverseArr(arr))

arr = [3,5]
print(arr)
print(reverseArr(arr))