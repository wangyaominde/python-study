class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1)+len(nums2))%2==0 and nums1!=[] and nums2!=[]:
            if min(nums1)<min(nums2):
                print("nums1<nums2")
            else:
                print("nums1>nums2")



        """minn = min(min(nums1),min(nums2))
        maxn = max(max(nums1),max(nums2))
        print(minn,maxn)
        arr = (maxn+minn)/2
        print(arr)"""



nums1 = [1,2]
nums2 = [3,4]
#print(nums1,nums2)
Solution.findMedianSortedArrays(None,nums1,nums2)
