from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = list()
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while (i < len(s)):
            j = i 
            while (s[j] != "#"): j+=1 

            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j            

        return res
    

strs = ["Hello","World"]
encode_str = "5#Hello5#World"
print(Solution().decode(encode_str))