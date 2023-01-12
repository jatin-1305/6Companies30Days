class Solution {
public:
    void inorder1(TreeNode* root, vector<int>& avg) {
        if(root!=NULL) {
            inorder1(root->left,avg);
            avg.push_back(root->val);
            inorder1(root->right,avg);
        }
        else return;
    }
    void inorder(TreeNode* root, int &ans) {
        if(root!=NULL) {
            inorder(root->left,ans);

            vector<int> avg;
            inorder1(root,avg);
            int av = (accumulate(avg.begin(),avg.end(),0)/avg.size());
            if(av==root->val) ans++;

            inorder(root->right,ans);
        }
        else return;
    }
    int averageOfSubtree(TreeNode* root) {
        int ans=0;
        inorder(root,ans);
        return ans;
    }
};
