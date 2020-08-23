'''
import collections

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)


s = 'a'
t = 'b'

ss = Solution()

print(ss.isAnagram(s,t))
'''
'''
class MyPoints:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def addX(self):
        self.x += 1

    def addY(self):
        self.y += 1

    def isEqual(self):
        return self.x == self.y

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        #po = MyPoints(0,0)
        #for i in 'abcdefghijklmnopqrstuvwxyz' :
        #    myDict[i] = po

        i = 0
        while i<len(s):
            if any(myDict) and any(myDict[s[i]]):
                myDict[s[i]].addX
                print(s[i],myDict[s[i]].x)
            else:
                myDict[s[i]] = MyPoints(1,0)

            #po.addX
            i+=1

        i = 0 
        while i<len(t):
            if any(myDict[t[i]]):
                myDict[t[i]].addY
                print(t[i],myDict[t[i]].y)
            else:
                myDict[t[i]] = MyPoints(0,1)
            #po.addY
            i+=1

        for key,value in myDict.items():
            #po = values
            print(key,value.x,value.y)
            if not value.isEqual :
                return False 
        return True 

'''
class Solution(object):
    def isAnagram(self, s, t):
    	if sorted(s) == sorted(t):
    		return True
    	else:
    		return False

s = Solution()
print(s.isAnagram('a','b'))

