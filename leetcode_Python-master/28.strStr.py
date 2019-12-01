class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if(needle in haystack):
            return(haystack.find(needle))
        else:
            return(-1)


haystack = "hello"
needle = "aa"
s = Solution()
s.strStr(haystack, needle)
