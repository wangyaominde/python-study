# @Author: wangyaomin  
# @Date: 2019-02-25 11:49:09  
# @Last Modified by:   wangyaomin  
# @Last Modified time: 2019-02-25 11:49:09

class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':
        return bin(int(a,2)+int(b,2))[2:]


a = "1010"
b = "1011"
s=Solution()
print(s.addBinary(a,b))