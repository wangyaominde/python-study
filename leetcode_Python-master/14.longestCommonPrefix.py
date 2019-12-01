# -*- coding: utf-8 -*-
#-code by wangyaomin-#

# ["flower","flow","flight"]


"""class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        if(len(strs)==0):
            return res

        sort = strs[0]
        for str in strs:
            if(len(sort)>len(str)):
                sort = str
        for x in range(len(strs)):
            for i in range(len(sort)):
                if(sort[i]!=strs[x][i]):
                    return res;
            res = res + sort[i]
        return res;
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        temp =""
        if len(strs)==0:
            return temp

        sort = strs[0]
        for str in strs:
            if len(sort) > len(str):
                sort = str
        for i in range(0,len(sort)):
            for j in range(0,len(strs)):
                if strs[j][i]!=sort[i]:
                    return temp;
            temp = temp + sort[i]
        return temp;

a = Solution()
print(a.longestCommonPrefix(["a","aa"]))
