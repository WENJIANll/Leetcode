# 输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
#
# 序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。
#
#  
#
# 示例 1：
#
# 输入：target = 9
# 输出：[[2,3,4],[4,5]]
# 示例 2：
#
# 输入：target = 15
# 输出：[[1,2,3,4,5],[4,5,6],[7,8]]
#  
#
# 限制：
#
# 1 <= target <= 10^5
from typing import List


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        def getlast(target):
            sum = 0
            for i in range(2,100000+1):
                sum = sum + i
                if sum > target:
                    break
            return i
        index = getlast(target)
        res = []
        expenddict = {}
        flag = 0
        for i in range(index,1,-1):
            sum = 0
            while not flag:
                for j in range(1,i+1):
                    sum = sum + j
                    expenddict[j] = sum
                flag = 1

            if expenddict[i] <= target and (target - expenddict[i] )% i == 0:
                subres = []
                for m in range(1, i + 1):
                    head = (target - expenddict[i]) // i + m
                    subres.append(head)
                res.append(subres)
        return res

s = Solution()
print(s.findContinuousSequence(15))

