'''
Given a sorted array in non-decreasing order, return an array of squares of each number, also in non-decreasing order. 

For example:[-4,-2,-1,0,3,5] -> [0,1,4,9,16,25]

Hint: How can you do it in O(n) time?
Doing this problem in O(nlog(n)) time is pretty trivial - just square all the numbers and then sort them.
In this case though, the interviewer is specifically looking for an O(n) time solution.
There is a pattern in the input array. The largest squares will be at either end of the array.
The lowest -ve number and the highest +ve number will be the largest squares. 
So, if we look at either ends of the array, we can go inwards and find smaller squares.
[-4, -2, -1, 0, 3, 5] -> 25, 16
Go inwards:[-4, -2, -1, 0, 3, 5] -> 9, 4
This will give us squares in descending order - from largest to smallest.
'''

def sortSquares(arr):
    output = []

    start = 0
    end = len(arr) - 1

    while (start<=end):
        if abs(arr[start]) > abs(arr[end]):
            output = [arr[start]**2] + output
            start = start + 1
        else:
            output = [arr[end]**2] + output
            end = end - 1
    return output

arr = [-4,-2,-1,0,3,5]
print(arr)
print(sortSquares(arr))

arr = [0,3,5]
print(arr)
print(sortSquares(arr))

arr = [-4,-2,-1]
print(arr)
print(sortSquares(arr))

arr = []
print(arr)
print(sortSquares(arr))

arr = [6]
print(arr)
print(sortSquares(arr))