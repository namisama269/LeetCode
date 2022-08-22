class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        int n = intervals.size();        
        vector<vector<int>> ans;
                
        for (int i = 0; i < n; ++i) {
            // no collision left
            if (intervals[i][1] < newInterval[0]) {
                ans.push_back(intervals[i]);
            }
            // no collision right
            else if (newInterval[1] < intervals[i][0]) {
                ans.push_back(newInterval);
                ans.insert(ans.end(), intervals.begin() + i, intervals.end());
                return ans;
            } else {
                newInterval[0] = min(newInterval[0], intervals[i][0]);
                newInterval[1] = max(newInterval[1], intervals[i][1]);
            }
            
        }
        
        ans.push_back(newInterval);
        return ans;
    }
};