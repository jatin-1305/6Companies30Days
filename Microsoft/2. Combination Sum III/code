class Solution {
public:
    void find(int ind, int target, int size, vector<int> &arr, vector<vector<int>> &ans, vector<int> &data) {
        if(target==0){
            if(data.size()==size){
                ans.push_back(data);
            }
            return;
        }
        for(int i=ind;i<arr.size();i++) {
            if(i>ind and arr[i]==arr[i-1]) continue;
            if(arr[i]>target) break;

            data.push_back(arr[i]);
            find(i+1,target-arr[i],size,arr,ans,data);
            data.pop_back();
        }
    }

    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> arr = {1,2,3,4,5,6,7,8,9};
        vector<int>data;
        vector<vector<int>> ans;
        find(0,n,k,arr,ans,data);
        return ans;
    }
};
