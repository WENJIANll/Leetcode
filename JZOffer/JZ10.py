# 剑指Offer10 - I.斐波那契数列
# 写一个函数，输入n ，求斐波那契（Fibonacci）数列的第n项。斐波那契数列的定义如下：
#
# F(0) = 0, F(1) = 1
# F(N) = F(N - 1) + F(N - 2), 其中N > 1.
# 斐波那契数列由0和1开始，之后的斐波那契数就是由之前的两数相加而得出。
# 答案需要取模
# 1e9 + 7（1000000007），如计算初始结果为：1000000008，请返回1。
# 示例 1：
# 输入：n = 2
# 输出：1
#
# 示例2：
# 输入：n = 5
# 输出：5
#
# 提示：0 <= n <= 100
class Solution:
    def fib(self, n: int) -> int:
        def returnfib(n):
            a = 0
            b = 1
            nextcount = 1
            while nextcount <= n:
                yield b
                a,b=b,a+b

        if n == 0:
            res = 0
        else:
            fibfib = returnfib(n)
            for i in range(n):
                res = next(fibfib)
        return res % 1000000007

s = Solution()
print(s.fib(5))