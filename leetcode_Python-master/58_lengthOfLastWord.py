# @Author: wangyaomin  
# @Date: 2019-02-25 09:15:02  
# @Last Modified by:   wangyaomin  
# @Last Modified time: 2019-02-25 09:15:02
class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        end = 123
        for i in s.split(" "):
            if(i != ''):
                end = i
        if(end == 123):
            return(0)
        else:return(len(end))

s = "a 123 "
S = Solution()
print(S.lengthOfLastWord(s))