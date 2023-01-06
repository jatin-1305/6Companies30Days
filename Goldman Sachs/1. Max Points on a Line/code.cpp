class Solution {
public:
    int maxPoints(vector<vector<int>>& points) {
        int mx = 1, n=points.size();
        
        for(int i=0;i<n-1;i++){
            map<double, int> mp;
            for(int j=i+1;j<n;j++){
                if(points[j][1]==points[i][1])      mp[-1000]++;
                else{ 
                    double x = (double)(points[j][0]-points[i][0])/(double)(points[j][1]-points[i][1]);
                    mp[x]++;
                }
            }
            int temp = 0;
            for(auto it:mp)
                temp = max(temp, it.second+1);    // +1 for the point[i]
            mx = max(temp, mx);
        }
        return mx;
    }
};
