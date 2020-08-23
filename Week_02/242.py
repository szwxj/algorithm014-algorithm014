import collections

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
        return self.isAnagram3(s,t)

    def isAnagram1(self, s: str, t: str) -> bool:
        return collections.Counter(s) == collections.Counter(t)
    
    def isAnagram2(self, s: str, t: str) -> bool:
    	if sorted(s) == sorted(t):
    		return True
    	else:
    		return False


    def isAnagram3(self, s: str, t: str) -> bool:
        myDict = {}
        #po = MyPoints(0,0)
        #for i in 'abcdefghijklmnopqrstuvwxyz' :
        #    myDict[i] = MyPoints(0,0)

        i = 0
        while i<len(s):
            if any(myDict) and (myDict.get(s[i],None) != None):
                myDict[s[i]].addX()
                print(s[i],myDict[s[i]].x)
            else:
                myDict[s[i]] = MyPoints(1,0)
            i+=1

        i = 0 
        while i<len(t):
            if any(myDict) and (myDict.get(t[i],None) != None):
                myDict[t[i]].addY()
                print(t[i],myDict[t[i]].y)
            else:
                myDict[t[i]] = MyPoints(0,1)
            i+=1

        for key,value in myDict.items():
            #print(key,value.x,value.y)
            if not value.isEqual() :
                return False 
        return True 


s = Solution()
print(s.isAnagram('abbc','baac'))

