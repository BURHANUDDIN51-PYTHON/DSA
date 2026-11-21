from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        max_water = 0 
        while (i < j):
            can_store = ((j-i) * min(heights[i], heights[j]))

            # Assign to the max_water
            if can_store > max_water: max_water = can_store


            # Move the pointers
            if heights[i] < heights[j]:
                i += 1 
            else:
                j -= 1



        return max_water





height = [2,2,2]
# height = [1,7,2,5,4,7,3,6]
print(Solution().maxArea(height))