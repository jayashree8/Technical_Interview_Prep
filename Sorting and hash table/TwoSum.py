'''
Given an array of integers, find a pair of integers that sums to a number Target.
For e.g, if A = [6,3,5,2,1,7]. Target = 4, Result= [3,1]
'''

'''
Method 1: Brute force approach
Pseudocode: 
for i: 0 to a.length-1
    for j: i+1 to a.length
        if a[i]+a[j] == target
            return pair (a[i],a[j])
'''
def two_sum_brute(a,target):
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i]+a[j]==target:
                return([a[i],a[j]])
    return None
print('Brute force approach')
print(two_sum_brute([6,3,5,2,1,7],4))
print(two_sum_brute([3,5,2,7],4))
print(two_sum_brute([1,0],1))
print(two_sum_brute([1],1))

'''
Method 2: Hash set approach
Pseudocode:
Initialize empty hash set
for i: 0 to a.length
    if target-a[i] in hash set
        return pair (a[i],target-a[i])
    else
        add a[i] in hash set
'''
def two_sum_hash(a,target):
    d = {}
    for i in range(len(a)):
        if target-a[i] in d.keys():
            return([a[i],target-a[i]])
        else:
            d[a[i]] = 'placeholder'
    return None
print('Hash set approach')
print(two_sum_hash([6,3,5,2,1,7],4))
print(two_sum_hash([3,5,2,7],4))
print(two_sum_hash([1,0],1))
print(two_sum_hash([1],1))