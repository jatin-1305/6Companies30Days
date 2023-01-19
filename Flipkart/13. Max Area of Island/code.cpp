class Solution {
public:
    void dfs(int i, int j, int &r, int &c, vector<vector<int>>& grid, vector<vector<int>> &vis, int &area) {
        if(i<0 || j<0 || i>=r || j>=c || grid[i][j]==0 || vis[i][j]) return;
        vis[i][j]=1;

        area++;
        dfs(i-1,j,r,c,grid,vis,area);
        dfs(i+1,j,r,c,grid,vis,area);
        dfs(i,j-1,r,c,grid,vis,area);
        dfs(i,j+1,r,c,grid,vis,area);
    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int r = grid.size();
        int c = grid[0].size();
        vector<vector<int>> vis(r, vector<int> (c,0));
        int ans = 0;
        for(int i=0;i<r;i++) {
            for(int j=0;j<c;j++) {
                if(!vis[i][j]) {
                    int area=0;
                    dfs(i,j,r,c,grid,vis,area);
                    ans = max(ans,area);
                }
            }
        }
        return ans;
    }
};
