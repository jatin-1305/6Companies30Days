class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        viewMap = defaultdict(int)
        maxViewMap = {}
        maxViews = 0
        
        for c,i,v in zip(creators,ids,views):
            viewMap[c] += v
            maxViews = max(maxViews,viewMap[c])
            if c not in maxViewMap or maxViewMap[c][1] < v or (maxViewMap[c][1] == v and i < maxViewMap[c][0]):
                maxViewMap[c] = [i,v]
        
        res = []
        for c in viewMap :
            if viewMap[c] == maxViews :
                res.append([c,maxViewMap[c][0]])
        return res
