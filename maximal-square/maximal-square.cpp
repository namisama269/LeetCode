class Solution {
    
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(); int n = matrix[0].size();
        int dp[300][300];
        memset(dp, 0, sizeof(dp));
        int ans = -1;
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || j == 0)
                    dp[i][j] = matrix[i][j] - '0';
                else if (matrix[i][j] == '1')
                    dp[i][j] = 1 + min(dp[i-1][j-1], min(dp[i][j-1], dp[i-1][j]));
                ans = max(dp[i][j], ans);
            }
        }
        
        return ans*ans;
    }
};