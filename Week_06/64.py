from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        #动态规划
        #dp = [[]]
        for i in range(0,len(grid)):
            for j in range (0,len(grid[i])):
                if i==0 and j==0 : grid[i][j] = grid[i][j]
                elif i==0 : grid[i][j] = grid[i][j-1] + grid[i][j]
                elif j==0 : grid[i][j] = grid[i-1][j] + grid[i][j]
                else : grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
        
        return grid[len(grid)-1][len(grid[0])-1]

s = Solution()

g = [[1,3,1],[1,5,1],[4,2,1]]

print(s.minPathSum(g))
