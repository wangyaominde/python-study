class Solution:
    def match(str):
        a = len(str)
        while a:
            a-=1
            b=a
            while b>=0:
                if(str[a]==str[b]):
                    if (a is not b):
                        #print(str[b:a])
                        return str[b:a]
                b-=1

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        return(Solution.match(s))
        '''a = len(s)
        while a:
            a-=1
            b=a
            while b>=0:
                if(s[a]==s[b]):
                    if (a is not b):
                        print(s[b:a])
                b-=1
'''





a = Solution()
s = "bbbb"
a.lengthOfLongestSubstring(s)
