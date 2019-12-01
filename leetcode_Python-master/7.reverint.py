# -*- coding: utf-8 -*-
#-code by wangyaomin-#


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 先把传过来的数变成字符串，匹配负号，使用切片反转，再转回数字返回
        test = str(x)
        if(test[0] == '-'):
            c = (int('-' + test[:0:-1]))
        else:
            c = (int(test[::-1]))
        if(c > 2147483647 or c < -2147483648):
            return 0
        else:
            return c


a = Solution()
# print(a.reverse(123))
print(a.reverse(123))
