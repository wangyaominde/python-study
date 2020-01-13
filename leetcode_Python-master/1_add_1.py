# -*- coding: utf-8 -*-
#-code by wangyaomin-#
def twoSum(nums, target):
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
