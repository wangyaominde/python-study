#----coding------#


'''
#Solution1
import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        return(np.median(nums1+nums2))

a = Solution()
nums1 = [1,2]
nums2 = [3,4]
print(a.findMedianSortedArrays(nums1,nums2))
'''
#Solution2

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        nums3=[]
        for x in nums1:
            for y in nums2:
                if(x<y):
                    nums3.append(x)
                else:
                    nums3.append(y)
        return nums3


s = Solution()
nums1 = [1,5]
nums2 = [3,4]
print(s.findMedianSortedArrays(nums1,nums2))
