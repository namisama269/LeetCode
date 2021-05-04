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
    int maxDepth(TreeNode* root) {
        int md = 0;
        search(root, 0, &md);
        return md;
    }
    void search(TreeNode* root, int depth, int *md) {
        if (depth > *md) 
            *md = depth;
        if (!root) 
            return;
        search(root->left, depth+1, md);
        search(root->right, depth+1, md);
    }
};