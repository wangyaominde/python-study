class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        leng1 = len(nums1)
        if leng1 % 2 == 0:
            midnums1 = (leng1 / 2 + leng1 / 2 + 1) / 2
        return midnums1
        # return (nums1, nums2)


nums1 = [1, 3]
nums2 = [2]
a = Solution
print(a.findMedianSortedArrays(a, nums1, nums2))
