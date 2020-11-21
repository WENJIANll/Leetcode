# 输入一个字符串，打印出该字符串中字符的所有排列。
#
#  
#
# 你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。
#
#  
#
# 示例:
#
# 输入：s = "abc"
# 输出：["abc","acb","bac","bca","cab","cba"]
#
from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        if len(s) == 1 : return [s]
        s = [c for c in s]
        curr = [[]]
        for c in s:
            curr = [l[:i] + [c] + l[i:] for l in curr for i in range(len(l) + 1)]
        return list(set(["".join(l) for l in curr]))

s = Solution()
print(s.permutation('abc'))