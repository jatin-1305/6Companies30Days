class Solution {
public:
    int minimumCardPickup(vector<int>& cards) {
     unordered_map<int,int>m;
     for(auto i: cards) m[i]=-1;
     int ans=INT_MAX;
     int track=0;
     for(int i=0;i<cards.size();i++) {
         if(m[cards[i]]==-1) {
             m[cards[i]] = i;
             track++;
         }
         else {
             ans = min(ans,i-m[cards[i]]+1);
             m[cards[i]]=i;
         }
     }
    return track==cards.size() ? -1 : ans;
    }
};
