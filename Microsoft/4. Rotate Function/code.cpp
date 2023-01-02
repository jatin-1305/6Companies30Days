class Solution {
public:
    int maxRotateFunction(vector<int>& nums) {
        int sum = accumulate(nums.begin(),nums.end(),0);
        int cal=0;
        for(int i=0;i<nums.size();i++) {
            cal += (i*nums[i]);
        }
        int ans=cal;
        for(int ele=nums.size()-1;ele>-1;ele--) {
            cal = cal+sum-(nums.size()*nums[ele]);
            ans = max(ans,cal);
        }
        return ans;
    }
};
