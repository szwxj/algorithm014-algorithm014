学习笔记
<br>
第860题：<br>
这道题应该不用复杂的算法，基本思路很简单：<br>
1、创建一个list；<br>
2、按顺序统计收入5和10元的数量；<br>
3、如果收入不是5，则需要找零，找零就是减少5和10的统计数量；<br>
4、判断5或10的数量是否小于0；<br>
easy<br>

题目：122题<br>
class Solution:<br>
    def maxProfit(self, prices: List[int]) -> int:<br>
        return sum(prices[i] - prices[i-1]    for i in range(1,len(prices))  if prices[i] - prices[i-1]>0)<br>

这种解体思路正确吗，有点不明白？<br>

看了题解，明白了，连续上涨交易日，连续交易等同于每天交易！！！<br>
可不能再范上周的错误了，没有执行git add 命令！！！