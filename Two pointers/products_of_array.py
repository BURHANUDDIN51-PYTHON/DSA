from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] * nums[i - 1]

        sufix_sum = [0] * n
        sufix_sum[n - 1] = nums[n - 1]
        for j in range(n-2, -1, -1):
            sufix_sum[j] = sufix_sum[j + 1] * nums[j + 1]
        
        res = [0] * n
        for i in range(n):
            res[i] = prefix_sum[i] * sufix_sum[i]
        return res

nums = [1,2,4,6]
print(Solution().productExceptSelf(nums))