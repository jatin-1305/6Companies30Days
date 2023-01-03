class Solution(object):
    def findUnsortedSubarray(self, nums):
        l=nums[:]
        l.sort()
        count,left,right=0,0,0
        for i in range(len(nums)):
            if l[i]!=nums[i]:
                left = i
                break
        for i in range(len(nums)-1,-1,-1):
            if l[i]!=nums[i]:
                right = i
                break
        if left==0 and right==0:
            return 0
        elif left==right:
            return 1
        return right-left+1
