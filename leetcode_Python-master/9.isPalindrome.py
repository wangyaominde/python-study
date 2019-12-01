# -*- coding: utf-8 -*-
#-code by wangyaomin-#


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        test = str(x)
        if (test == test[::-1]):
            return True
        else:
            return False
