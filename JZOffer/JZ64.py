# 剑指Offer64.求1 + 2 +…+n
# 求1 + 2 + ... + n ，要求不能使用乘除法、for 、 while 、 if 、 else 、switch、case等关键字及条件判断语句（A?B:C）。
#
# 示例
# 1：
# 输入: n = 3
# 输出: 6
#
# 示例2：
# 输入: n = 9
# 输出: 45
#
# 限制：
# 1 <= n <= 10000

class Solution:
    def __init__(self):
        self.res = 0
    def sumNums(self, n: int) -> int:

        def sumsum(n):
            self.res += n
            return n and sumsum(n-1)
        sumsum(n)
        return self.res

s = Solution()
print(s.sumNums(5))

