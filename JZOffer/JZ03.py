# 找出数组中重复的数字。
#
# 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，
# 但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
#
# 示例 1：
#
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        lenn = len(nums)
        sett = dict()
        for i in range(lenn):
            if sett.get(nums[i]) == None:
                sett[nums[i]] = 1
            else:
                return nums[i]


s = Solution()
print(s.findRepeatNumber([0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]))
