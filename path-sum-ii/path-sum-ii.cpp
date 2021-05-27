/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    vector<vector<int>> solns;
    vector<int> curr;
    void dfs(TreeNode *root, int targetSum) {
        // base case if root is NULL
        if (!root)
            return;
        // add node's value to current sum
        curr.push_back(root->val);
        // if at a leaf, check if the target is reached
        if (!root->left && !root->right) {
            if (targetSum == root->val) {
                solns.push_back(curr);
            }
        }   
        // search on left and right subtrees
        dfs(root->left, targetSum - root->val);
        dfs(root->right, targetSum - root->val);
        // undo adding the current node when backtracking
        curr.pop_back();
    }
public:
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        dfs(root, targetSum);
        return solns;
    }
};
