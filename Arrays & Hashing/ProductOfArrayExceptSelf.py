from typing import List

class Solution:
    def productOfArrayExceptSelf(self, arr: List[int]) -> List[int]:
        result = [1] * len(arr)
        prefix = 1
        postfix = 1

        for i in range(len(arr)):
            result[i] = prefix 
            prefix = prefix * arr[i]

        for i in range(len(arr) - 1, -1, -1):
            result[i] = postfix * result[i]
            postfix = postfix * arr[i]
        return result
    
nums = Solution()
print(nums.productOfArrayExceptSelf([1,2,4,6])) # [48,24,12,8]

nums2 = Solution()
print(nums2.productOfArrayExceptSelf([-1,0,1,2,3])) # [0,-6,0,0,0]
