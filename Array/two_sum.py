from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Two pointer 
        i = 0
        j = len(nums) - 1
        sum = 0

        while (i < j):

            sum = nums[i] + nums[j]
            if abs(sum) > abs(target):    
                j -= 1
            elif abs(sum) < abs(target):
                i += 1
            else: 
                return [i,j] 

        return [-1,-1]


sol = Solution()
nums=[-10,-1,-18,-19]
target=-19


# print(sol.twoSum(nums, target))

sort_nums = sorted(nums)

print(sort_nums, reverse=True)



