# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
#
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#
# 示例 2：
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        wide = len(matrix)
        if wide != 0 :
            long = len(matrix[0])
        else:
            return []
        outlist = []
        num = 0
        self.sub(matrix, long, wide, outlist, num)
        return outlist

    def sub(self,alist,long,wide,outlist,num):
        L = len(alist[0])
        W = len(alist)
        if long > 0 and wide > 0:
            if long == 1 and wide == 1:
                outlist.append(alist[num][num])
            elif wide == 1:
                for top in range(long):
                    outlist.append(alist[num][top+num])
            elif long == 1:
                for right in range(wide):
                    outlist.append(alist[num+right][L - 1 -num])
            else:
                for top in range(long - 1 ):
                    outlist.append(alist[num][top+num])
                for right in range(wide - 1 ):
                    if long == 2 :
                        print(alist[num+right])
                    outlist.append(alist[num+right][L - 1 - num ])
                for low in range(long - 1 ):
                    outlist.append(alist[W - 1 - num][L -1 -num -low])
                for left in range(wide - 1 ):
                    outlist.append(alist[W -1 -num -left][num])
            long = long - 2
            wide = wide - 2
            num = num + 1
            self.sub(alist,long,wide,outlist,num)

S = Solution()
l = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(S.spiralOrder(l))

