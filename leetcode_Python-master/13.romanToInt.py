# -*- coding: utf-8 -*-
#-code by wangyaomin-#


class Solution:
    def romanToInt(self, str):
        """
        :type s: str
        :rtype: int
        """
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        rtnum = 0
        for i in range(len(str)):
            if i < len(str) - 1 and rom[str[i]] < rom[str[i + 1]]:
                rtnum -= rom[str[i]]
            else:
                rtnum += rom[str[i]]
        return rtnum
