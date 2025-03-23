from typing import List

'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

def containsDuplicate(nums: List[int]) -> bool:
    numsSet = set(nums)
    if len(numsSet) == len(nums):
        return False
    else:
        return True
    

print(containsDuplicate([1,2,3,1])) # True
print(containsDuplicate([1,2,3,4])) # False
