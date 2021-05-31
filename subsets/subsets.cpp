class Solution {
    vector<vector<int>> ans;
    vector<int> subset;
    void solve(vector<int>& nums, int k) {
        if (k == nums.size()) {
            ans.push_back(subset);
            return;
        }
        solve(nums, k+1);
        subset.push_back(nums[k]);
        solve(nums, k+1);
        subset.pop_back();
    }
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        solve(nums, 0);
        return ans;
    }
};