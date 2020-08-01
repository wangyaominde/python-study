#----coding------#
import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        return(np.median(nums1+nums2))

a = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(a.findMedianSortedArrays(nums1,nums2))