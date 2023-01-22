class Solution {
public:
    
    void dfs(int i, int j, vector<vector<int>> &grid, int n, int m, bool &isClosed) {
        if(i < 0 || j < 0 || i >= n || j >= m || grid[i][j] != 0)
            return;
        
        isClosed &= checkClosedIsnald(i, j, n, m);
        grid[i][j] = 2;
        
        dfs(i+1, j, grid, n, m, isClosed);
        dfs(i-1, j, grid, n, m, isClosed);
        dfs(i, j+1, grid, n, m, isClosed);
        dfs(i, j-1, grid, n, m, isClosed);
    }
    
    bool checkClosedIsnald(int i, int j, int n_rows, int n_cols) {
        if(i == 0 || j == 0 || i == n_rows-1 || j == n_cols-1)
                return false;
        return true;
    }
    
    int closedIsland(vector<vector<int>>& grid) {
        int n_rows = grid.size(), n_cols = grid[0].size();
        int nClosedIslands = 0;
        for(int i = 0; i < n_rows; i++) {
            for(int j = 0; j < n_cols; j++) {
                if(grid[i][j] == 0) {
                    bool isClosed = true;
                    dfs(i, j, grid, n_rows, n_cols, isClosed);
                    nClosedIslands += isClosed;
                }
            }
        }
        return nClosedIslands;
    }
};
