# -*- coding: utf-8 -*-
#-code by wangyaomin-#
def twoSum(nums, target):
    lang = len(nums)
    i = 0
    o = 0
    for i in range(lang):
        for o in range(i):
            if nums[i] + nums[o] == target:
                if i != o:
                    return[o, i]


print(twoSum(nums, target))
