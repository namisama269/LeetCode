class Solution {
public:
    void floodFill(vector<vector<char>>& grid, int x, int y, int m, int n) {
        if (x < 0 || y < 0 || x >= m || y >= n || grid[x][y] == '0') 
            return;
        grid[x][y] = '0';
        floodFill(grid, x-1, y, m, n);
        floodFill(grid, x+1, y, m, n);
        floodFill(grid, x, y-1, m, n);
        floodFill(grid, x, y+1, m, n);
    }
    
    int numIslands(vector<vector<char>>& grid) {
        int ans = 0;
        int m = grid.size();
        int n = grid[0].size();
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == '1') {
                    floodFill(grid, i, j, m, n);
                    ++ans;
                }
            }
        }
        
        return ans;
    }
};