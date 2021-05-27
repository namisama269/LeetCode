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
public:
    bool hasPathSum(TreeNode* root, int targetSum) {
        return dfs(root, targetSum);
    }
    bool dfs(TreeNode *root, int targetSum) {
        // base case if root is NULL
        if (!root)
            return false;
        // if at a leaf, check if the target is reached
        if (!root->left && !root->right)
            return targetSum == root->val;
        
        bool l = dfs(root->left, targetSum - root->val);
        bool r = dfs(root->right, targetSum - root->val);
        return (l || r);
    }
};