/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool doValidBST(struct TreeNode *node, long lower, long upper);

bool isValidBST(struct TreeNode* root){
    return doValidBST(root, LONG_MIN, LONG_MAX);
}

bool doValidBST(struct TreeNode *node, long lower, long upper) {
    if (node == NULL) {
        return true;
    }
    if (!(node->val >= lower && node->val <= upper)) {
        return false;
    }
    long val = node->val;
    return doValidBST(node->left, lower, val - 1) && doValidBST(node->right, val + 1, upper);
}