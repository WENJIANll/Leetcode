# 剑指Offer40.最小的k个数

# 输入整数数组arr ，找出其中最小的k个数。例如，输入4、5、1、6、2、7、3、8
# 这8个数字，则最小的4个数字是1、2、3、4。
#
# 示例1：
# 输入：arr = [3, 2, 1], k = 2
# 输出：[1, 2]
# 或者[2, 1]

# 示例2：
# 输入：arr = [0, 1, 2, 1], k = 1
# 输出：[0]
# 限制：
#
# 0 <= k <= arr.length <= 10000
# 0 <= arr[i] <= 10000
from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        res = []
        index = 0
        mincount = 0
        lenofarr = len(arr)
        while mincount < k :
            minvalue = arr[0]
            if minvalue in res:
                index += 1
                continue
            curmincount = 1
            for i in range(1,lenofarr):
                if minvalue < arr[i]:
                    pass
                elif minvalue > arr[i]:
                    minvalue = arr[i]
                    curmincount = 1
                elif minvalue == arr[i]:
                    curmincount += 1
            for j in range(curmincount):
                res.append(minvalue)
                arr.remove(minvalue)
            mincount += curmincount
            lenofarr = len(arr)
        lenofres = len(res)
        if lenofres > k:
            for m in range(lenofres-k):
                res.pop()
        return res
s = Solution()
arr = [3,0,3,1,5,1,8,9,0]
k = 4
print(s.getLeastNumbers(arr,k))