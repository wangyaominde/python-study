class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        temp = 0
        d = {}
        start = 0
        for i in range(len(s)):
            if s[i] in d and start <= d[s[i]] :
                print("start:",start)
                start = d[s[i]] +1
            temp = max(i-start+1,temp)
            d[s[i]] = i
            print("d:",d,"temp:",temp)
        return temp

a = Solution()
s = "abcabcabc"
print(a.lengthOfLongestSubstring(s))

"""a="abcabcabc"
if "abc" in a:
    print("yes")
else :
    print("no")"""
