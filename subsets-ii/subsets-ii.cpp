class Solution {
    set<vector<int>> ans;
    vector<int> subset;
    void solve(vector<int>& nums, int k) {
        if (k == nums.size()) {
            ans.insert(subset);
            return;
        }
        solve(nums, k+1);
        subset.push_back(nums[k]);
        solve(nums, k+1);
        subset.pop_back();
    }
public:
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        solve(nums, 0);
        vector<vector<int>> out(ans.begin(), ans.end());
        return out;
    }
};