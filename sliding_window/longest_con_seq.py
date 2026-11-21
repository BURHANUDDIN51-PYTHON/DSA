from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numset = set(nums)

        for num in numset:
            if (num - 1) not in numset:
                # Start the sequence here 
                length = 1 
                while (num + 1) in numset: 
                    length += 1 
                    num += 1 
                res = max(length, res)
        return res


nums = [0,3,2,5,4,6,1,1]
print(Solution().longestConsecutive(nums=nums))