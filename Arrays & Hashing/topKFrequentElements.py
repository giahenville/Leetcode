from typing import List
from collections import defaultdict

'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
'''

def topKElements(nums: List[int], k: int) -> List[int]:


    numsMap = {} #int: int

    for num in nums:
        if num in numsMap:
            numsMap[num] += 1
        else:
            numsMap[num] = 1

    numsList = [ [] for _ in range(len(nums) + 1) ]
    
    for num in numsMap:
        numsList[numsMap[num]].append(num)
    
    result = []
    # print("numsMap: ", numsMap, "numsList: ", numsList)
    for i in range(len(numsList) - 1, -1, -1):
        for j in range(len(numsList[i])):
            result.append(numsList[i][j])
            if len(result) == k:
                return result



print(topKElements([1,1,1,2,2,3], 2)) # [1, 2]
print(topKElements([1], 1)) # [1]
