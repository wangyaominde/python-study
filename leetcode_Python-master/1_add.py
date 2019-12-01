# -*- coding: utf-8 -*-
#-code by wangyaomin-#
'''def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for num1,num2 in enumerate(nums):
        num2 = target - num1
        if num2 in nums:
            y = nums.index(num2)
            x = nums.index(num1)
            if y != x:
                return [y,x]
'''


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
