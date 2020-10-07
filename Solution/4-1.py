# 给定两个大小为m和n的正序（从小到大）数组nums1和nums2。请你找出并返回这两个正序数组的中位数。
#首先考虑特殊情况
#①有负数存在
#②有数组为空
#③
#
#
#
# 进阶：你能设计一个时间复杂度为
# O(log(m + n))
# 的算法解决此问题吗？

# 示例1：
# 输入：nums1 = [1, 3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1, 2, 3] ，中位数 2
# 示例2：
# 输入：nums1 = [1, 2], nums2 = [3, 4]
# 输出：2.50000
# 解释：合并数组 = [1, 2, 3, 4] ，中位数(2 + 3) / 2 = 2.5
# 示例3：
# 输入：nums1 = [0, 0], nums2 = [0, 0]
# 输出：0.00000
# 示例4：
# 输入：nums1 = [], nums2 = [1]
# 输出：1.00000
# 示例5：
# 输入：nums1 = [2], nums2 = []
# 输出：2.00000
from typing import List


#这两个数组是有序的那么可以去除A数组中的一个依次和B数组中的元素比较，
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = nums1.__len__()
        l2 = nums2.__len__()
        nodeid = 0
        if nums2 == [] or nums1 == []:
            if nums2 == []:
                nums2 = nums1
        else:
            head1 = nums1[0]
            head2 = nums2[0]
            tail1 = nums1.pop()
            tail2 = nums2.pop()
            nums1.append(tail1)
            nums2.append(tail2)
            if head1 >= tail2:
                nums2 = nums2.__add__(nums1)
            elif head2 >= tail1:
                nums2 = nums1.__add__(nums2)
            else:
                for i in nums1:
                    l = len(nums2)
                    #注意nodeid和l的比较一个是长度，一个是索引，它们之间差1
                    if nodeid < l:
                        for j in nums2[nodeid:]:
                            if j >= i:
                                jindex = nums2.index(j)
                                nums2.insert(jindex,i)
                                jindex = nums2.index(j)
                                nodeid = jindex
                                print('nodeid:' + nodeid.__str__())
                                break  # 注意使用break
                        else:
                            iindex = nums1.index(i)
                            print(iindex)
                            nums2 = nums2.__add__(nums1[iindex:])
                            break
                    elif len(nums2) == l1+l2:
                        break

        l = len(nums2)
        print(nums2)
        if l%2 == 0:
            midindex = l // 2
            midnum = (nums2[midindex-1] + nums2[midindex]) / 2
        else:
            midindex = ((l+1) // 2)
            midnum = nums2[midindex-1]
        return midnum

S = Solution()
# nums1 = [1,3,6,24,84,123,555]
# nums2 = [2,3,5,8,12,34,55]

# nums1 = [1,3]
# nums2 = [-1,5]

# nums1 = [-1,-3]
# nums2 = [2]

# nums1 = [3]
# nums2 = [-2,-1]

# nums1 = []
# nums2 = [-2,-1]

# nums1 = [1,3,45]
# nums2 = [2]

nums1 = [1,2,5]
nums2 = [-1,3]

outnum = S.findMedianSortedArrays(nums1,nums2)
print(outnum)




























