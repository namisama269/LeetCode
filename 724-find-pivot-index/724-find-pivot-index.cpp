class Solution {
public:
    int pivotIndex(vector<int>& nums) {
        int sum = 0;
        for (auto n: nums) sum += n;
        
        int curr = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if ((sum - nums[i]) % 2 == 0 && (sum - nums[i]) / 2 == curr) return i;
            curr += nums[i];
        }
        
        return -1;
    }
};