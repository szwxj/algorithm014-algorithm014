class Solution:
    def climbStairs(self, n: int) -> int:
        #分治
        s0 = 0
        s1 = 0
        r = 1
        if n < 2 : return 1
        for i in range(1,n+1):
            s0 = s1
            s1 = r
            r = s1 + s0
        return r

s = Solution()

for i in range(0,10):
    print(i,s.climbStairs(i))
