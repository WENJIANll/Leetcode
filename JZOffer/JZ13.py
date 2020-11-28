# 地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，它每次可以向左、右、上、下移动一格
# （不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。
# 但它不能进入方格 [35, 38]，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
#
# 提示：
#
# 1 <= n,m <= 100
# 0 <= k <= 20

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        resdict = {}
        x , y = 0 , 0
        def getcount(x,y):
            if x >= 0 and x < n and y >= 0 and y < m:
                m_hundred = x // 100
                m_ten = (x % 100) // 10
                m_unitt = (x % 100) % 10
                n_hundred = y // 100
                n_ten = (y % 100) // 10
                n_unitt = (y % 100) % 10
                thple = (x,y)
                while m_hundred+m_ten+m_unitt+n_hundred+n_ten+n_unitt <= k and resdict.get(thple,1):
                    resdict[thple] = 0
                    getcount(x+1,y)
                    getcount(x-1,y)
                    getcount(x,y+1)
                    getcount(x,y-1)
        getcount(x,y)
        return len(resdict.keys())

s = Solution()
print(s.movingCount(5,4,7))