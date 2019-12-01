# -*- coding: utf-8 -*-
#-code by wangyaomin-#
#有问题，稍后修改#

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = {')':'(', ']':'[', '}':'{'}
        l = [None]
        for i in s:
            if i in a and a[i] == l[-1]:
                l.pop()
            else:
                l.append(i)
        return len(l)==1

s = "{}"
a = Solution()
a.isValid(s)
