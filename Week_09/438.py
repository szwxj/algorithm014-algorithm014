from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #排序 + join
        n = len(p)
        p = "".join(sorted(p))
        res = []
        for i in range(len(s)-n+1):
            if "".join(sorted(s[i:i+n])) == p:
                res.append(i)        
        return res

s = "cbaebabacd" 
p = "abc"

ss = Solution()
print(ss.findAnagrams(s,p))