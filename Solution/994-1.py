# 994.腐烂的橘子
# 在给定的网格中，每个单元格可以有以下三个值之一：
# 值 0 代表空单元格；
# 值 1 代表新鲜橘子；
# 值 2 代表腐烂的橘子。
# 每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。
#
# 返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1
from typing import List

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] 仅为 0、1 或 2

# [[2,1,1],[1,1,0],[0,1,1]]
# 时间超32%，空间超70%
class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        l = len(grid)
        # 初始化一个存储各样橘子坐标的的字典
        dict = {}
        dict[0] = []
        dict[1] = []
        dict[2] = []
        # 纵坐标
        for y in range(l):
            # 初始化l2，因为题目没说，每个grid[y]长度相等
            l2 = len(grid[y])
            # 横坐标
            for x in range(l2):
                if grid[y][x] == 0:
                    dict[0].append([y,x])
                if grid[y][x] == 1:
                    dict[1].append([y,x])
                if grid[y][x] == 2:
                    dict[2].append([y,x])
        # 如果新鲜句子为0，则符合题目没有新鲜句子，返回0
        if len(dict[1]) == 0:
            return 0
        elif len(dict[2]) == 0:
            return -1
        # 腐烂橘子和正常橘子都不为0，则开始判断
        else:
            return  self.nextto(dict[2], dict[1])


    # 遍历two中的每个元素，和one中每个元素比较x，y坐标，是否符合要求，如果符合那么one中的x，y坐标元素下一分钟将会腐烂，将之加入two中
    def nextto(self, two, one):
        minet = 0
        while len(one) > 0 :
            lone = len(one)
            ltwo = len(two)
            # 处理过的two元素列表
            withtwolist = []
            lasttwo = two[ltwo-1]
            for i in range(ltwo):
                twoi = two[i]
                yy = twoi[0]
                xx = twoi[1]
                withtwolist.append(twoi)
                # 符合要求，也就是下一秒会腐烂的橘子列表
                withonelist = []
                for j in range(len(one)):
                    if (one[j][0] == yy and abs(one[j][1] - xx) == 1) or (one[j][1] == xx and abs(one[j][0] - yy) == 1):
                        withonelist.append(one[j])
                # 将已经确定下一秒会腐烂的橘子在one中去除，这样遍历下一个two元素是就不需要比较这个了
                for withindex1 in range(len(withonelist)):
                    if one.count(withonelist[withindex1]) > 0:
                        one.remove(withonelist[withindex1])
                    # 这里不必担心对two列表的修改会影响i和twoi的值，因为来源是range(ltwo)，已经定住了
                    two.append(withonelist[withindex1])
            #将two遍历一遍之后，更新two列表，将遍历过的two元素删除掉，并对当前情况做判断（是否可以继续腐烂）
            for withindex2 in range(len(withtwolist)):
                if two.count(withtwolist[withindex2]) > 0:
                    two.remove(withtwolist[withindex2])
            if two == [] and one != []:
                return -1
            elif two == [] or (two[len(two)-1] == lasttwo):
                return minet
            else:
                minet = minet + 1
        return minet

# [[2,2,2],[1,1,0],[0,1,1]]
# [[2,2,2,1,1,1,1,1,1],[],[0,1,1]]

S =Solution()
# out = S.orangesRotting([[2,2,2],[1,1,0],[0,1,1]])
out = S.orangesRotting([[2,2,2,1,1,1,1,1,1],[],[0,1,1]])

print(out)

