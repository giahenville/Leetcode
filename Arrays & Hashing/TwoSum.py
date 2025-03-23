from typing import List
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
'''

def twoSum(nums: List[int], target: int) -> List:
    # iterate over list, 
    # store elements and their index in map,
    # get number needed to add up to target
    # check if in map
    # return indexes
    
    numsMap = {}
    for index, num in enumerate(nums):
        numNeeded = target - num
        if  numNeeded in numsMap:
            return [index, numsMap[numNeeded]]
        else:
            numsMap[num] = index

print(twoSum([1, 7, 5, 2], 8)) #[1, 0]
print(twoSum([1, 7, 5, 2], 12)) #[1, 2]
