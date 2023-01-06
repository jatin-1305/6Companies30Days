class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
           int boom = 0;
           int n = points.size();
           if(n < 3) return 0;
       
            for(int i = 0; i<n; i++){
                map<int, int> mp;
                for(int j = 0; j<n; j++){
                    if(i == j) continue;
                    int dist = (points[i][0] - points[j][0]) * (points[i][0] - points[j][0]);
                    dist +=   ((points[i][1] - points[j][1]) * (points[i][1] - points[j][1]));
                    mp[dist]++;
                }
                
                for(auto it : mp){
                    if(it.second <= 1) continue;
                    boom += (it.second * (it.second - 1));
                }
            }
        return boom;
    }
};
