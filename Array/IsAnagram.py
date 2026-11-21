from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping

        # create the mappings 
        for s in strs:
            # Found the mappings 
            count = [0]*26 #a ... z
            for char in s:
                count[ord(char) - ord('a')] += 1 

            res[tuple(count)].append(s)

        return list(res.values())





        
strs=["act","pots","tops","cat","stop","hat"]
print(Solution().groupAnagrams(strs))