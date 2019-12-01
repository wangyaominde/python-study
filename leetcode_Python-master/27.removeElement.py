# -*- coding: utf-8 -*-
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x = 0
        for i in range(len(nums)):
            if (nums[i] != val):
                nums[x] = nums[i]
                x += 1
        return(x)


nums = [3, 2, 2, 3]
val = 3
s = Solution()
s.removeElement(nums, val)
