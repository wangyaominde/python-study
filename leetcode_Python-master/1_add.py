# -*- coding: utf-8 -*-
#-code by wangyaomin-#
class Solution:
    def twoSum(self,nums, target):
        lang = len(nums)
        i = 0
        o = 0
        for i in range(lang):
            for o in range(i):
                if nums[i] + nums[o] == target:
                    if i != o:
                        return[o, i]

nums = [2, 7, 11, 15]
target = 9
s=Solution()
s.twoSum(nums,target)
