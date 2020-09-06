from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        s5 = s10 = 0
        for k in bills:
            if k == 5 : 
                s5 += 1
            elif k == 10 :
                s10 += 1
                s5 -= 1
            elif k == 20 :
                if s10 >0 :
                    s10 -= 1 
                    s5 -= 1  
                else :
                    s5 -= 3
            if s5 <0 or s10 < 0 :
                return False
        return True

b = [5,5,5,10,20]
s = Solution()
print(s.lemonadeChange(b))
