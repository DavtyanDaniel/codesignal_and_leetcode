# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
#
# The overall run time complexity should be O(log (m+n)).
# link to problem is https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        a = nums1 + nums2
        a.sort()
        l = len(a)

        if l < 2:
            return a[0]
        if l % 2 == 0:
            return(a[l//2]+a[(l//2)-1])/2
        else:
            return a[l//2]

