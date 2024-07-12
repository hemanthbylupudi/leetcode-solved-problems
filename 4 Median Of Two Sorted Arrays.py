class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1=sorted(nums1)
        mid_ind=len(nums1)//2
        if(len(nums1)%2==1):
            res=float(nums1[mid_ind])
        else:
            res= (nums1[mid_ind]+nums1[mid_ind-1])/2
        return float(res)
