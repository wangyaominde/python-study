# -*- coding: utf-8 -*-
#-code by wangyaomin-#


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = 0
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]]:
                start = d[s[i]] + 1
            temp = max(i - start + 1, temp)
            d[s[i]] = i
        return temp


a = Solution()
s = "ads"
print(a.lengthOfLongestSubstring(s))
