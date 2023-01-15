class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        size,ans = len(nums[0]),[]
        for k,trim in queries:
            # store the trimmed numbers in list as -> list of int of number and its index
            # example, l= [[2,0],[3,1],[1,2],[4,3]], here "2","3","1","4" are trimmed part and 0,1,2,3 are indexes
            # starting index for trim will be [len(nums[i])-trim :]
            l = sorted([[int(i[size-trim:]),ind] for ind,i in enumerate(nums)])
            # after sorting the list append the k-1's [1] index from sorted list
            ans.append(l[k-1][1])
        return ans
