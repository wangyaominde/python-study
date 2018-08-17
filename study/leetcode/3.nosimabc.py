class Solution:
    def lengthOfLongestSubstring(self, s):
        slen = len(s)
        for i in range(slen):
            for x in range(slen):
                if s[x]==s[i]:
                    print(s[x:i])

a = Solution()
s = "abcabcbb"
a.lengthOfLongestSubstring(s)
