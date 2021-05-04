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
    int minDepth(TreeNode* root) {
        if (!root)
            return 0;
        int md = INT_MAX;
        search(root, 1, &md);
        return md;
    }
    void search(TreeNode *root, int depth, int *md) {
        if (depth >= *md) 
            return;
        if (!root)
            return;
        if (!root->left && !root->right && depth < *md)
            *md = depth;
        search(root->left, depth+1, md);
        search(root->right, depth+1, md);
    }
};