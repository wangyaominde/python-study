# @Author: wangyaomin  
# @Date: 2019-03-04 10:25:48  
# @Last Modified by:   wangyaomin  
# @Last Modified time: 2019-03-04 10:25:48

class Solution:
    def mySqrt(self, x: 'int') -> 'int':
        if(x==0 or x==x*x):
            return x

        for i in range(1,x):
            if((i*i)<=x and (i+1)*(i+1)>x):
                return(i)




S=Solution()
x=1
S.mySqrt(x)