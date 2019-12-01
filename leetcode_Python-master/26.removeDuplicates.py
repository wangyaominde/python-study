class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 1):
            return nums
        x = 0
        for i in range(len(nums)):
            if(nums[i] != nums[i - 1]):
                nums[x] = nums[i]
                x += 1
        return(x)


nums = [1]
s = Solution()
s.removeDuplicates(nums)
