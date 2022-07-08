'''
Given an array of numbers, replace each even number with two of the same number. 
e.g, [1,2,5,6,8, , , ,] -> [1,2,2,5,6,6,8,8].
Assume that the array has the exact amount of space to accommodate the result.
'''
def FindLastNumber(arr):
    lastnum = len(arr)-1
    while (lastnum>=0 and arr[lastnum]==-1):
        lastnum = lastnum - 1
    return lastnum

def CloneEvenNumbers(arr):
    if (len(arr)==0):
        return arr
    end = len(arr)
    i = FindLastNumber(arr)
    while (i>=0):
        num = arr[i]
        if num%2==0:
            end = end - 1
            arr[end] = num
            end = end - 1
            arr[end] = num
        else:
            end = end - 1
            arr[end] = num
        i = i - 1
    return (arr)

arr = [1,2,5,6,8,-1,-1,-1]
print(arr)
print(CloneEvenNumbers(arr))

arr = [1]
print(arr)
print(CloneEvenNumbers(arr))

arr = [2,-1]
print(arr)
print(CloneEvenNumbers(arr))

arr = []
print(arr)
print(CloneEvenNumbers(arr))