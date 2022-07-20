'''
 Given a sorted array of integers, find two numbers in the array that sumto a given integer target.
 
 For example, if a = [1,2,3,5,6,7] and target = 11, the answer will be 5 and 6.

 Hint: Traverse array from start and end and assume array is sorted and return the index
'''

def twoSum(arr, target):
    start = 0
    end = len(arr) - 1
    while (start<end):
        val = arr[start] + arr[end]
        if val < target:
            start = start + 1
        elif val > target:
            end = end - 1
        else:
            return (start,end)
    return 0

arr = [1,2,3,5,6,7]
target = 11
print(arr)
print(target)
print(twoSum(arr, target))

arr = [1,2,3,5,6]
target = 12
print(arr)
print(target)
print(twoSum(arr, target))

arr = [1]
target = 1
print(arr)
print(target)
print(twoSum(arr, target))

arr = [2,3,4,5]
target = 7
print(arr)
print(target)
print(twoSum(arr, target))