from sortedcontainers import SortedList
class Solution(object):
    # nums1[i] - nums1[j] <= nums2[i] - nums2[j] + diff
    # nums1[i] - nums2[i] <= nums1[j] - nums2[j] + diff
    def numberOfPairs(self, nums1, nums2, diff):
        n=len(nums1)
        count=0
        l=SortedList()
        for i in range (n):
            greater = l.bisect_right(nums1[i]-nums2[i]+diff)
            count+=greater
            l.add(nums1[i]-nums2[i])
        return count
