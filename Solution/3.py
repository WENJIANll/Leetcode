
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = -1
        len_of_s = len(s)
        max_sub_len = 0

        while right <= len_of_s - 1:
            beforset = len(s[left:right + 1])
            afterset = len(set(s[left:right + 1]))
            if afterset == beforset:
                max_sub_len = max(afterset,max_sub_len)
                right = right + 1
            else:
                left = left + 1
        return max_sub_len


s = Solution()
print(s.lengthOfLongestSubstring('abcabcbb'))

