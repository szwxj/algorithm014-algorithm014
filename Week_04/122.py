from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return sum(prices[i] - prices[i-1]  for i in range(1,len(prices)) if prices[i] > prices[i-1])

p = [7,1,5,3,6,4]
s = Solution()
print(s.maxProfit(p))

