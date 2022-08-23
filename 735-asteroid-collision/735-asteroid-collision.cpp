class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> ans;
        
        for (int i = 0; i < asteroids.size(); ++i) {
            ans.push_back(asteroids[i]);
            int m = ans.size();
            while (m >= 2 && (ans[m-2] > 0 && ans[m-1] < 0)) {
                if (abs(ans[m-1]) == abs(ans[m-2])) {
                    ans.pop_back();
                } else {
                    ans[m-2] = abs(ans[m-1]) > abs(ans[m-2]) ? ans[m-1] : ans[m-2];
                }
                ans.pop_back();
                m = ans.size();
            }
        }
        
        return ans;
    }
};