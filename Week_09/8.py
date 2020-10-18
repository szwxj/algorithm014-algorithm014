import re

class Solution:
    def myAtoi(self, s: str) -> int:
        #return max(min(int(*re.findall('^[\+\-]?\d+', s.lstrip())), 2**31 - 1), -2**31)
        return self.myAtoi2(s)

    def myAtoi2(self, s: str)-> int:
        '''
        正则表达式的解释：  
        ^：匹配字符串开头  
        [\+\-]：代表一个+字符或-字符  
        ?：前面一个字符可有可无  
        \d：一个数字  
        +：前面一个字符的一个或多个  
        \D：一个非数字字符  
        *：前面一个字符的0个或多个  
        '''

        INT_MAX = 2147483647
        INT_MIN = -2147483648
        s = s.lstrip()      #清除左边多余的空格
        num_re = re.compile(r'^[\+\-]?\d+')   #设置正则规则
        num = num_re.findall(s)   #查找匹配的内容
        num = int(*num) #由于返回的是个列表，解包并且转换成整数
        return max(min(num,INT_MAX),INT_MIN)    #返回值

s = Solution()
print(s.myAtoi("42"))

