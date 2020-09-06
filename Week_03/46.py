from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(i) for i in itertools.permutations(nums, len(nums))]
        
a = [1,2,3]
s = Solution()
print(s.permute(a))
