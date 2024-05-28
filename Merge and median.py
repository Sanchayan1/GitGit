class Solution:
    def findMedianSortedArrays(self,nums1,nums2):
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1) % 2 == 0:
            return (nums1[len(nums1)//2] + nums1[len(nums1) // 2 - 1]) / 2
        else:
            return nums1[len(nums1)//2]

nums1=[1,2,3]
nums2=[7,8,9]
print(findMedianSortedArrays(nums1,nums2))
        
