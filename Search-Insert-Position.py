'''
Given a sorted array and a target value,
return the index if the target is found.
'''

from bisect import bisect, bisect_left


def searchInsert(nums, target):
    return bisect_left(nums, target)

print(searchInsert([1,3,5,6], 7))