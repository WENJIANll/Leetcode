# 面试题4.二维数组中的查找
# 在一个
# n * m
# 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个高效的函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
#
# 示例:
#
# 现有矩阵
# matrix
# 如下：
#
# [
#     [1, 4, 7, 11, 15],
#     [2, 5, 8, 12, 19],
#     [3, 6, 9, 16, 22],
#     [10, 13, 14, 17, 24],
#     [18, 21, 23, 26, 30]
# ]
# 给定
# target = 5，返回
# true。
#
# 给定
# target = 20，返回
# false。
from typing import List

class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        else:
            xlen = len(matrix[0])
            ylen = len(matrix)
            x = xlen / 2
            y = ylen / 2
            prex = 0
            prey = 0
            while not (abs(x - prex) == 1 or abs(y - prey) == 1):
                if matrix[y][x] > target:
                    prex,prey = x,y
                    y = y / 2
                    x = x / 2
                elif matrix[y][x] < target:
                    prex, prey = x, y
                    y = y + y/2
                    x = x + x/2
                elif matrix[y][x] == target:
                    return True

