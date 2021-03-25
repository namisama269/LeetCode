class Solution {
public:
    static bool sortKey(const vector<int>& d1, const vector<int>& d2) {
        return d1[0] > d2[0];
    }
    bool canFit(vector<int>& d1, vector<int>& d2) {
        return d1[0] < d2[0] && d1[1] < d2[1];
    }
    int maxEnvelopes(vector<vector<int>>& envelopes) {
        int n = envelopes.size();
        sort(envelopes.begin(), envelopes.end(), sortKey);
        vector<int> dp(n, 1);
        for (int i = 1; i < n; ++i) {
            int currMax = 0;
            for (int j = 0; j < i; ++j) {
                if (dp[j] > currMax && canFit(envelopes[i], envelopes[j])) {
                    currMax = dp[j];
                }
            }
            dp[i] = 1 + currMax;
        }
        return *max_element(dp.begin(), dp.end());
    }
};