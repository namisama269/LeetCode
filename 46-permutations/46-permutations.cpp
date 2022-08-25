class Solution {
public:
    void search(vector<vector<int>>& perms, vector<int>& perm, vector<bool>& chosen, vector<int>& nums, int n) {
        if (perm.size() == n) {
            perms.push_back(perm);
        } else {
            for (int i = 0; i < n; ++i) {
                if (chosen[i]) continue;
                chosen[i] = true;
                perm.push_back(nums[i]);
                search(perms, perm, chosen, nums, n);
                chosen[i] = false;
                perm.pop_back();
            }
        }
    }
    vector<vector<int>> permute(vector<int>& nums) {
        int n = nums.size();
        vector<int> perm;
        vector<vector<int>> perms;
        vector<bool> chosen(n, false);
        
        search(perms, perm, chosen, nums, n);
        
        return perms;
    }
};