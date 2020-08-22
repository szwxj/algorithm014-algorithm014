import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


s = 'a'
t = 'b'

ss = Solution()

print(ss.isAnagram(s,t))
