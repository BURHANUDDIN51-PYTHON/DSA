from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l, r = 0, k
        max_num = max(nums[l:r])
        res.append(max_num)

        for r in range(k, len(nums)):

            # Update the max elment if the new el is greater 
            if nums[r] >= max_num:
                max_num = nums[r]
                l += 1 
                res.append(max_num)
                continue
            
            # If left element is max_num or max_num is not the right most element 
            l += 1
            max_num = max(nums[l:r])
            res.append(max_num)

        return res

nums = [1,2,1,0,4,2,6]
k = 3
print(Solution().maxSlidingWindow(nums, k))