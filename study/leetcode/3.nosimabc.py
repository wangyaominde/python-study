class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = len(s)
        while a:
            a-=1
            b=a
            while b>=0:
                if(s[a]==s[b]):
                    if (a is not b):
                        print(s[b:a])
                b-=1






a = Solution()
st = "abc"
a.match(st)
